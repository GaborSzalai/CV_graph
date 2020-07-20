# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:42:40 2020

@author: gaborszalai
"""

import pandas as pd

nodes_df= pd.read_csv('nodes_data.csv')  

nodes=nodes.to_json(orient='records')