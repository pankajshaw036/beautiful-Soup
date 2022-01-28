#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page = requests.get('https://www.dineout.co.in/delhi-resturants/buffet-special')


# In[8]:


page


# In[6]:


# Page Content


# In[9]:


soup = BeautifulSoup(page.content)


# In[10]:


soup


# ## Scraping First Name

# In[16]:


#first, we will use html tag where we have the first title of the resturants.

first_title = soup.find('div',class_="restnt-info cursor")
first_title


# In[ ]:




