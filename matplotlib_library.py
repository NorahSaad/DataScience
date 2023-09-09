#!/usr/bin/env python
# coding: utf-8

#  #insert and print data set using pandas library,also represent it graphically using matplotlib library

# In[40]:


import pandas 
from pandas import DataFrame
import matplotlib.pyplot as plt


# In[41]:



z= pandas.read_csv('cost-revenue-clean.csv')


# In[42]:


z.describe()


# In[43]:


plt.figure( figsize=(10,6) )
x = DataFrame(z, columns=['production_budget_usd'])
y = DataFrame(z, columns=['worldwide_gross_usd'])
plt.scatter(x , y , alpha=0.3)
plt.title('Film Cost Vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Budget $')
plt.ylim( 0 , 2000000000 )
plt.xlim( 0 , 400000000 )
plt.show()


# In[ ]:




