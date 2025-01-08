import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import urllib.request

# Get request to the url
url = 'https://companiesmarketcap.com/tesla/revenue/'
response = requests.get(url)

# Verify if the request is successful
if response.status_code==200:
  # Scrape information from web page with BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')
  
# Get revenue data
revenue = soup.find(class_='table')

data=[]
for x in revenue.find_all("td"):
  data.append(x.get_text())

# Select only years data
years= data[::3]

# Get the first 4 characters of each year and convert to integer
for i in range(len(years)):
  years[i] = int(years[i][0:4])

# Select only revenue data
revenue_data= data[1::3]

# Get the second to the sixth characters of each revenue data and convert to float
for i in range(len(revenue_data)):
  revenue_data[i] = float(revenue_data[i][1:6])

# Create a dictionary with the two lists
result = {'Year': years, 'Revenue': revenue_data}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(result)
print(df)

# Bar chart
plt.figure(figsize = (10, 5))
plt.bar(years, revenue_data)
plt.title("Bar chart")
plt.show()









