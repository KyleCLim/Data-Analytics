# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 18:06:05 2025

@author: Kyle
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- format of read_csv

# data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv', sep=';')

# summary of the data
data.info()

# Playing around with variables
var = True

# Definig variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Mathematical Operations on Tablue
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation

# CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# Adding a new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost
data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost)/Cost
data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

# Rounding Markup
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# Combining data fields
# my_date = data['Day']+'-'

# Change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

# Checking columns data type
print(day.dtype)
print(year.dtype)
print(data['Day'].dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

# Using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.head(5) #brings in first 5 rows
data.iloc[:,2] #brings in all rows on the 2nd column
data.iloc[4,2] #brings in 4th row, 2nd column

# Using split to split client keywords field
# new_var = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand=True)

# Creating new column for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

# using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to merge files
#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# Merge files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

# Dropping columns
# df = df.drop('column name', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

# Export into a csv
data.to_csv('ValueInc_Cleaned.csv', index = False)







