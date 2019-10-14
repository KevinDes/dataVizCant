# -*- coding: utf-8 -*-
"""
Created on Wed Oct 9 10:51:36 2019

@author: cantrelle
"""

import pandas as pd
import numpy as np
from collections import Counter


def get_mean(df, mode=False):
    
    # mode (bouléen) : pour avoir le mode des variables catégorielles
    
    res = []
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for var in list(df):
        if df[var].dtypes in numerics:
            res.append(df[var].mean())
        else:
            if mode==False:
                res.append(np.nan)
            else:
                res.append(Counter(df[var].dropna(axis=0)).most_common(1)[0][0])
    return res
    
def get_se(df):
    res = []
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for var in list(df):
        if df[var].dtypes in numerics:
            res.append(df[var].var())
        else:
            res.append(np.nan)
    return res

def get_min(df):
    res = []
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for var in list(df):
        if df[var].dtypes in numerics:
            res.append(df[var].min())
        else:
            res.append(np.nan)
    return res

def get_max(df):
    res = []
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for var in list(df):
        if df[var].dtypes in numerics:
            res.append(df[var].max())
        else:
            res.append(np.nan)
    return res

def get_occ_et_val_princi(df):
    res = []
    l=[]
    j=0
    for i in df.columns:
        l = list(df[i].value_counts().to_dict().items())[:min(3, len(df[i].value_counts()))]
        res.append(l)
       # for j in range(len(list(df[i].value_counts().to_dict().items())[:min(3, len(df[i].value_counts()))])):
       #     res.append(l[j])
    return res
  

def indicator(df, mode=False, chemin2save = None):
    
    resume = pd.DataFrame(columns=['Variable', 'Type', 'Taux_NA',
                              'Nb_unique','occ_et_val_princi', 'Moyenne', 'Variance',
                              'Min',
                              'Max'])
    resume['Variable'] = list(df)
    
    resume['occ_et_val_princi'] = get_occ_et_val_princi(df)
    
    resume['Type'] = list(df.dtypes)
    resume['Taux_NA'] = list(df.isnull().sum()/df.shape[0])
    resume['Nb_unique'] = [df[var].nunique() for var in list(df)]
    resume['Moyenne'] = get_mean(df, mode=mode)
    resume['Variance'] = get_se(df)
    #resume['Variance_normalisee'] = resume['Moyenne']/resume['Variance']
    resume['Min'] = get_min(df)
    resume['Max'] = get_max(df)
    if (chemin2save != None):
        resume.to_csv(chemin2save)
    return resume



