#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np


# In[2]:



stat_capacity_df = pd.read_csv("https://raw.githubusercontent.com/Amould1/Project_2/master/stat_capacity.csv")
stat_capacity_df


# In[3]:



stat_capacity_df_clean = stat_capacity_df.drop(["Indicator Code", "Indicator Name", "1960",
                                                "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968",
                                               "1969",  "1970","1971", "1972", "1973", "1974", "1975", "1976", "1977",
                                                "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986",
                                                "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", 
                                                "1996", "1997", "1998","1999", "2000", "2001", "2002", "2003", "2003",
                                                "2004", "2005", "2006", "2007", "2008", "2009", "2019"], axis=1)
stat_capacity_df_clean


# In[4]:


final_stat_capacity_df = stat_capacity_df_clean.rename(columns={'2010': '2010 : Stat Capacity Score',
                                                                '2011': '2011 : Stat Capacity Score',
                                                                '2012': '2012 : Stat Capacity Score',
                                                                '2013': '2013 : Stat Capacity Score',
                                                                '2014': '2014 : Stat Capacity Score',
                                                                '2015': '2015 : Stat Capacity Score',
                                                                '2016': '2016 : Stat Capacity Score',
                                                                '2017': '2017 : Stat Capacity Score',
                                                                '2018': '2018 : Stat Capacity Score',})
final_stat_capacity_df


# In[5]:


preparedness = pd.read_csv("https://raw.githubusercontent.com/Amould1/Project_2/master/Preparedness_data.csv")


# In[6]:


preparedness.head()


# In[7]:


codes = pd.read_csv("https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv")
codes.head()


# In[9]:



codes_limited = codes[["alpha-3", "name"]]
codes_limited.columns = ["Country Code", "Country"]
codes_limited.head()


# In[10]:


preparedness_codes = preparedness.merge(codes_limited, how = "inner",  on = "Country")
new_preparedness_codes = preparedness_codes.rename(columns={'2010': '2010 : Preparedness Score',
                                                                '2011': '2011 : Preparedness Score',
                                                                '2012': '2012 : Preparedness Score',
                                                                '2013': '2013 : Preparedness Score',
                                                                '2014': '2014 : Preparedness Score',
                                                                '2015': '2015 : Preparedness Score',
                                                                '2016': '2016 : Preparedness Score',
                                                                '2017': '2017 : Preparedness Score',})


# In[11]:



combined_df = new_preparedness_codes.merge(final_stat_capacity_df, how = "inner",  on = "Country Code")
new_combined = combined_df.drop(["2018 : Stat Capacity Score", "Country"], axis=1)
new_combined


# In[31]:



new_combined_df = new_combined[["Country Name", "Country Code",
                                "2017 : Preparedness Score", "2017 : Stat Capacity Score",]]
new_combined_df


# In[36]:



new_combined_df = new_combined.nlargest(10,'2017 : Stat Capacity Score')[["Country Name", "Country Code",
                                "2017 : Preparedness Score", "2017 : Stat Capacity Score",]]
new_combined_df


# In[42]:


df=new_combined_df

df.plot(kind='bar')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax = df.plot.bar(x='Country Name')
plt.title('Top 10 Statistcal Capacity Scores of 2017')
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.5))
plt.show()


# In[ ]:




