# Import necessary libraries
import pandas as pd




#Read the dataset
df = pd.read_csv('US_Accidents_Dec21_updated.csv')# Display the first few rows of the dataset
print(df.head())# Display basic information about the dataset
print(df.info())# Check for missing values in each column
print(df.isnull().sum())# Display summary statistics of the dataset
print(df.describe())# Display the first few rows of the dataset