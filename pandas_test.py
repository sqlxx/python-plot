#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:58:12 2021

@author: sqlxx
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

df1 = pd.DataFrame(dict(x=["a", "b", "c"], y=range(1,4))) 

df = pd.DataFrame({'x':['A', 'B', 'C', 'A', 'C'], '2010':[1,3,4,4,3], '2011':[3,5,2,8,9]})
df_melt = pd.melt(df, id_vars=['x'], var_name='year', value_name='value')


print(type(df_melt['year'].astype(int))) # A series
print(type(df_melt[['year']].astype(int))) # A Data Frame

df_row_sum = df[['2010', '2011']].apply(lambda x: x.sum(), axis=1)


madf = pd.read_csv("MappingAnalysis_Data.csv")
group = ["0%(Control)", "1%", "5%", "15%"]
fig = plt.figure(figsize=(4,3), dpi=100)
for i in range(0, 4):
    temp_df = madf[madf.variable==group[i]]
    plt.plot(temp_df.Time, temp_df.value)
plt.xlabel("Time(d)", fontsize=14)
plt.ylabel("value", fontsize=12)
plt.plot()

df1 = madf[madf.variable=="0%(Control)"]
df2 = madf[madf.variable=="1%"]
df3 = madf[madf.variable=="5%"]

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(8,3))
ax0.plot(df1.Time, df1.value)
ax0.plot(df2.Time, df2.value)

ax1.plot(df1.Time, df1.value)
ax1.plot(df3.Time, df3.value)

p = (ggplot(madf, aes(x='Time', y='value'))+
geom_point(shape='o', color='black', fill="#336A97", stroke=0.25, alpha=0.8))
p.draw()
