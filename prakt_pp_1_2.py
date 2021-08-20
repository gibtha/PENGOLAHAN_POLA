# -*- coding: utf-8 -*-
"""PRAKT_PP_1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-WzOavuYPr_NhKAxPLBA458F1PK9qnK_
"""

import numpy as sp
import pandas as pd
import matplotlib.pyplot as plt

f = pd.read_csv("http://www.exploredata.net/ftp/Spellman.csv")
print(f)

traffic = sp.genfromtxt("https://raw.githubusercontent.com/aricarmona/machine-learning-python/master/data/web_traffic.tsv", delimiter='\t')

#mengambil sepuluh data pertama
print(traffic[:10])

#mengetahui size data [baris,kolom]
print(traffic.shape)

x = traffic[:,0]
y = traffic[:,1]

#mengambil nilai x yang kolom y tidak Nan
x = x[~sp.isnan(y)]
#mengambil nilai y yang tidak Nan
y = y[~sp.isnan(y)]

print(x.shape)
#menampilkan plot bentuk scatter
plt.scatter(x,y)
plt.title("Web Traffic Last Month")
plt.xlabel("Time")
plt.ylabel("Hits/Hours")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
