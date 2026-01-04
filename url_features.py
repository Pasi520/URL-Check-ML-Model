#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
from urllib.parse import urlparse

high_risk = r"(verify|update|confirm|suspend|urgent|security-check)"
low_risk = r"(login|account|secure|signin|auth)"
tlds = ('.xyz', '.top', '.ru', '.info', '.club')

def extract_features(url):

    try:
        if not isinstance(url, str):
            return [0]*11

        parsed = urlparse(url)
        domain = parsed.netloc

        return [
            len(url),
            url.count('.'),
            url.count('-'),
            url.count('@'),
            url.count('//'),
            1 if url.startswith("https") else 0,
            1 if re.search(high_risk, url.lower()) else 0,
            1 if re.search(low_risk, url.lower()) else 0,
            1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,
            domain.count('.') - 1 if domain else 0,
            1 if domain.endswith(tlds) else 0
        ]

    except Exception:
        # invalid URL → safe fallback
        return [0]*11


# In[6]:


get_ipython().system('jupyter nbconvert --to python url_features.ipynb')


# In[ ]:





# In[ ]:





# In[ ]:




