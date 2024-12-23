#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Data Analyst Intern Assignment - Excel.xlsx')




# In[10]:


print(data.head())


# In[11]:


data['Age'].fillna(data['Age'].mean(), inplace=True)


# In[12]:


age_statistics = data['Age'].describe()


# In[13]:


data['Age'].hist(bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


# In[ ]:




