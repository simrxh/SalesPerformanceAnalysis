#!/usr/bin/env python
# coding: utf-8

# # Sales Performance Analysis
# 
# ## Objective
# This project analyzes sales transaction data to identify sales trends, top-performing product lines, strongest markets, and deal size patterns.
# 
# ## Tools Used
# - Python
# - Pandas
# - Matplotlib
# - Jupyter Notebook

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv", encoding="latin1")


# In[25]:


print(df.shape)
print(df.columns)
print(df.isnull().sum())


# In[26]:


df = df.drop_duplicates()


# In[27]:


print(df.shape)


# In[28]:


print(df.describe())


# In[29]:


print(df.columns.tolist())


# In[30]:


df_clean = df[['ORDERDATE', 'QUANTITYORDERED', 'SALES', 'PRODUCTLINE', 'COUNTRY', 'DEALSIZE']].copy()
print(df_clean.head())


# In[31]:


df_clean = df[['ORDERDATE', 'QUANTITYORDERED', 'SALES', 'PRODUCTLINE', 'COUNTRY', 'DEALSIZE']].copy()

df_clean['ORDERDATE'] = pd.to_datetime(df_clean['ORDERDATE'])

print(df_clean.head())


# In[32]:


import matplotlib.pyplot as plt

df_clean['MONTH'] = df_clean['ORDERDATE'].dt.to_period('M')

monthly_sales = df_clean.groupby('MONTH')['SALES'].sum()

print(monthly_sales)


# In[33]:


monthly_sales.plot(kind='line')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()


# In[34]:


productline_sales = df_clean.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)

print(productline_sales)


# In[35]:


productline_sales.plot(kind='bar')

plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.show()


# In[36]:


country_sales = df_clean.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

print(country_sales)


# In[37]:


top_10_countries = country_sales.head(10)

top_10_countries.plot(kind='bar')

plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.show()


# In[38]:


deal_sales = df_clean.groupby('DEALSIZE')['SALES'].sum().sort_values(ascending=False)

print(deal_sales)


# In[39]:


deal_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Sales Distribution by Deal Size")
plt.ylabel("")

plt.show()


# ### Insight: Deal Size Analysis
# 
# Medium-sized deals generated the highest total sales in the dataset. This shows that most revenue came from mid-sized customer purchases. The business can focus on maintaining medium-sized deals while also finding ways to increase large deal opportunities.

# In[40]:


deal_count = df_clean['DEALSIZE'].value_counts()

print(deal_count)


# In[41]:


deal_count.plot(kind='bar')

plt.title("Number of Orders by Deal Size")
plt.xlabel("Deal Size")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.show()


# In[42]:


top_productline = productline_sales.idxmax()
top_productline_sales = productline_sales.max()

top_country = country_sales.idxmax()
top_country_sales = country_sales.max()

top_dealsize = deal_sales.idxmax()
top_dealsize_sales = deal_sales.max()

most_common_dealsize = deal_count.idxmax()
most_common_dealsize_count = deal_count.max()

print("INSIGHTS SUMMARY")
print("----------------")
print(f"1. The highest revenue-generating product line is {top_productline}, with total sales of ${top_productline_sales:,.2f}.")
print(f"2. The country with the highest sales is {top_country}, generating ${top_country_sales:,.2f}.")
print(f"3. The deal size contributing the most revenue is {top_dealsize}, with total sales of ${top_dealsize_sales:,.2f}.")
print(f"4. The most common deal size is {most_common_dealsize}, appearing in {most_common_dealsize_count} orders.")
print("5. Monthly sales trend analysis helps identify changes in sales performance over time.")


# 
# ### Insight: Product Line Performance
# 
# The product line with the highest total sales was Classic Cars. This shows that Classic Cars contributed the most revenue compared to other product categories. The business can focus more on high-performing product lines while also reviewing lower-performing categories for improvement.

# ### Insight: Country-wise Sales Performance
# 
# USA had the highest total sales, generating $3,627,982.83. This shows that USA was the strongest market in the dataset. Other countries had lower sales compared to USA, so the business can focus on maintaining strong sales in USA while exploring growth opportunities in lower-performing countries.

# ## Final Insights Summary
# 
# - Classic Cars generated the highest total sales, making it the strongest product line.
# - USA was the top-performing country by revenue, showing it was the strongest market.
# - Medium-sized deals contributed the highest sales, meaning mid-sized purchases were the main revenue driver.
# - Sales performance changed across months, which can help the business identify strong and weak sales periods.
# 
# ## Business Recommendation
# 
# The business should continue focusing on high-performing product lines like Classic Cars and strong markets like USA. It should also look for ways to increase large deals while maintaining medium-sized customer purchases.

# In[43]:


df_clean.to_csv("cleaned_sales_data.csv", index=False)


# In[ ]:




