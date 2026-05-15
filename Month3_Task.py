#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Watch"],
    "Sales": [50000, 30000, 20000, 10000, 15000],
    "Profit": [10000, 7000, 4000, 2000, 3000]
}

df = pd.DataFrame(data)

print(df)


# In[2]:


# Find:
#Mean ,Median ,Maximum , Minimum

print("Mean Sales:", df["Sales"].mean())
print("Median Sales:", df["Sales"].median())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())


# In[3]:


import matplotlib.pyplot as plt

plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


# In[5]:


# pie chart
plt.pie(df["Profit"],
labels=df["Product"],
autopct='%1.1f%%')

plt.title("Profit Distribution")
plt.show()


# In[6]:


#– Finding Trends & Insights
highest_sales = df[df["Sales"] == df["Sales"].max()]

print(highest_sales)


# In[7]:


#Correlation Analysis
correlation = df["Sales"].corr(df["Profit"])

print("Correlation:", correlation)


# In[8]:


# EDA
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())


# In[9]:


print(df.shape)


# In[10]:


print(df.columns)


# In[11]:


print(df.info())


# In[12]:


print(df.describe())


# In[13]:


print(df.isnull().sum())


# In[14]:


print(df.duplicated().sum())


# In[15]:


print("Total Revenue:", df["Total Revenue"].sum())


# In[16]:


print("Total Profit:", df["Total Profit"].sum())


# In[17]:


print("Total Profit:", df["Total Profit"].sum())


# In[18]:


highest_country = df.groupby("Country")["Total Revenue"].sum().sort_values(ascending=False)

print(highest_country.head(1))


# In[19]:


print(df["Item Type"].value_counts())


# In[20]:


print(df["Units Sold"].mean())


# In[21]:


correlation = df[["Units Sold","Total Revenue","Total Profit"]].corr()

print(correlation)


# In[22]:


import matplotlib.pyplot as plt

top_country = df.groupby("Country")["Total Revenue"].sum().sort_values(ascending=False).head(5)

top_country.plot(kind='bar')

plt.title("Top 5 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.show()


# In[23]:


df["Total Profit"].plot()

plt.title("Profit Trend")
plt.xlabel("Index")
plt.ylabel("Profit")

plt.show()


# In[24]:


sales_channel = df["Sales Channel"].value_counts()

plt.pie(sales_channel,
labels=sales_channel.index,
autopct='%1.1f%%')

plt.title("Sales Channel Distribution")

plt.show()


# In[25]:


plt.hist(df["Units Sold"])

plt.title("Units Sold Distribution")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")

plt.show()


# In[26]:


plt.scatter(df["Total Revenue"], df["Total Profit"])

plt.xlabel("Revenue")
plt.ylabel("Profit")
plt.title("Revenue vs Profit")

plt.show()


# In[27]:


high_profit = df[df["Total Profit"] > 500000]

print(high_profit)


# In[28]:


sorted_df = df.sort_values(by="Total Profit", ascending=False)

print(sorted_df.head())


# In[29]:


region_revenue = df.groupby("Region")["Total Revenue"].sum()

print(region_revenue)


# In[30]:


print("Total Revenue:", df["Total Revenue"].sum())

print("Total Profit:", df["Total Profit"].sum())

print("Average Units Sold:", df["Units Sold"].mean())

print("Top Selling Item:")
print(df["Item Type"].value_counts().head(1))


# In[ ]:




