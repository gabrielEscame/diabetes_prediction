import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('./public/data/pima-data.csv')

# Correlation visualisation
def data_correlation (data, filename, size=11):
  correlation = data.corr()
  fig, ax = plt.subplots(figsize=(size, size))
  ax.matshow(correlation)
  plt.xticks(range(len(correlation.columns)), correlation.columns)
  plt.yticks(range(len(correlation.columns)), correlation.columns)
  plt.savefig(f'./public/{filename}.jpg')

del data['skin']

# data_correlation(data, 'withoutskin')