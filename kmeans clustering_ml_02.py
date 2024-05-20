# -*- coding: utf-8 -*-
"""PRODIGY_ML_02

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cScGsrBJwHBPVReH8Yzn7vMGYA50gzjv
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df=pd.read_csv('/content/Mall_Customers.csv')
df

#preprocessing

df.isnull().sum()

df.duplicated().sum()

plt.scatter(df['Annual Income (k$)'],df['Spending Score (1-100)'])

#using elbow method to decide the number of cluster to be formed
krange=range(1,9)
sse=[]
for k in krange:
  model1=KMeans(n_clusters=k)
  model1.fit(df[['Annual Income (k$)','Spending Score (1-100)']])
  sse.append(model1.inertia_)

sse

plt.plot(krange,sse)

#n_cluster=5

scaler=MinMaxScaler()
scaler.fit(df[['Annual Income (k$)']])
df['Annual Income (k$)']=scaler.transform(df[['Annual Income (k$)']])

scaler.fit(df[['Spending Score (1-100)']])
df['Spending Score (1-100)']=scaler.transform(df[['Spending Score (1-100)']])

df

model1=KMeans(n_clusters=5)
model1.fit(df[['Annual Income (k$)','Spending Score (1-100)']])

y=model1.predict(df[['Annual Income (k$)','Spending Score (1-100)']])
y

model1.cluster_centers_

df['New_Cluster']=y
df

df1=df[df.New_Cluster==0]
df2=df[df.New_Cluster==1]
df3=df[df.New_Cluster==2]
df4=df[df.New_Cluster==4]
df5=df[df.New_Cluster==5]

plt.scatter(df1['Annual Income (k$)'],df1['Spending Score (1-100)'],color="black")
plt.scatter(df2['Annual Income (k$)'],df2['Spending Score (1-100)'],color="red")
plt.scatter(df3['Annual Income (k$)'],df3['Spending Score (1-100)'],color="yellow")
plt.scatter(df4['Annual Income (k$)'],df4['Spending Score (1-100)'],color="red")
plt.scatter(df5['Annual Income (k$)'],df5['Spending Score (1-100)'],color="gray")
plt.scatter(model1.cluster_centers_[:,0],model1.cluster_centers_[:,1],color="blue",marker="*",label="centroids")
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()

