#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import matplotlib as cm
dataset=pd.read_csv("dataset2.txt",delimiter="\t")

L1_PC1 =np.array(dataset[25:36]["PC1"])
L2_PC1 =np.array(dataset[36:37]["PC1"])
L3_PC1 =np.array(dataset[37:48]["PC1"])
L4_PC1 =np.array(dataset[48:59]["PC1"])
L5_PC1 =np.array(dataset[59:70]["PC1"])
L6_PC1 =np.array(dataset[70:81]["PC1"])

L1_PC2 =np.array(dataset[25:36]["PC2"])
L2_PC2 =np.array(dataset[36:37]["PC2"])
L3_PC2 =np.array(dataset[37:48]["PC2"])
L4_PC2 =np.array(dataset[48:59]["PC2"])
L5_PC2 =np.array(dataset[59:70]["PC2"])
L6_PC2 =np.array(dataset[70:81]["PC2"])

L1_PC3 =np.array(dataset[25:36]["PC3"])
L2_PC3 =np.array(dataset[36:37]["PC3"])
L3_PC3 =np.array(dataset[37:48]["PC3"])
L4_PC3 =np.array(dataset[48:59]["PC3"])
L5_PC3 =np.array(dataset[59:70]["PC3"])
L6_PC3 =np.array(dataset[70:81]["PC3"])
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
plt.rcParams['legend.fontsize'] = 10   

ax.plot(L1_PC1,L1_PC2,L1_PC3, 'b+', markersize=12,linewidth=50, alpha=0.5, label='H1')
ax.plot(L2_PC1,L2_PC2,L2_PC3, 'gd',markersize=8,linewidth=0, alpha=0.5, label='H2-Connatum')
ax.plot(L3_PC1,L3_PC2,L3_PC3, 'rh', markersize=8,linewidth=0.5, alpha=0.5, label='H3')
ax.plot(L4_PC1,L4_PC2,L4_PC3, 'co',markersize=8,linewidth=0, alpha=0.5, label='H4')
ax.plot(L5_PC1,L5_PC2,L5_PC3, 'mH', markersize=8,linewidth=0.5, alpha=0.8, label='H5')
ax.plot(L6_PC1,L6_PC2,L6_PC3, 'y*',markersize=12,linewidth=0.5, alpha=0.5, label='H6')


plt.title('PCoA SNP Verteilung')
ax.legend(loc='upper right')
ax.set_xlabel("PC1",fontsize=12)
ax.set_ylabel("PC2",fontsize=12)
ax.set_zlabel("PC3",fontsize=12)
#plt.savefig("PCoA_Analyse",dpi=300,tight_layout=True)
plt.show()
