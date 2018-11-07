#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:51:38 2018

@author: liuhangyu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 


df_list=[]

for i in range(2000,2019):
    result_lists=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    url="http://www.espn.com/nba/statistics/team/_/stat/team-comparison-per-game/sort/avgPoints/year/{0}".format(i)
    html=requests.get(url).content

	# print(html)
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    rows=soup.find('table').find_all('tr')
    for k in range(len(rows)):
        if k in [0,1,12,13,24,25]:
            continue
        results = rows[k].find_all('td')
        for j in range(len(results)):
            result_lists[j].append(results[j].getText())
    
    df_result = pd.DataFrame(result_lists[0])
    for k in range(1, len(result_lists)):
        tmp_s = pd.Series(result_lists[k])
        df_result[str(k)] = tmp_s.values
    
    df_list.append(df_result)
            

              
    
    
    
    
    
    
    
 
        
        
        
        
        
        
        
        
        
