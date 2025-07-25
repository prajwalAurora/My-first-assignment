✅ Step 1: Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style='whitegrid')


---

✅ Step 2: Load Dataset

Assume we have a dataset named housing.csv with fields like:

price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, zipcode, etc.


# Load the CSV
df = pd.read_csv("housing.csv")

# Display top 5 rows
df.head()


---

✅ Step 3: Basic Cleaning

# 1. Check missing values
print(df.isnull().sum())

# 2. Fill missing values (example: fill NA bedrooms with median)
df['bedrooms'].fillna(df['bedrooms'].median(), inplace=True)
df['bathrooms'].fillna(df['bathrooms'].median(), inplace=True)

# 3. Ensure correct data types
df['zipcode'] = df['zipcode'].astype(str)


---

✅ Step 4: Simple Transformation

Create a new feature: price per square foot

df['price_per_sqft'] = df['price'] / df['sqft_living']


---

✅ Step 5: Visualizations

📊 1. Distribution of House Prices

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()


---

📊 2. Relationship Between Sqft and Price

plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqft_living', y='price', data=df)
plt.title('Price vs. Living Area (Sqft)')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Price')
plt.show()


---

📊 3. Average Price by Zipcode (Top 10)

top_zipcodes = df.groupby('zipcode')['price'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_zipcodes.index, y=top_zipcodes.values, palette='viridis')
plt.title('Top 10 Zipcodes by Average Price')
plt.xlabel('Zipcode')
plt.ylabel('Average Price')
plt.show()
