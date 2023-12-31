# -*- coding: utf-8 -*-
"""kel5-estimasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dYiV6BtgAng8As0LcUq9GYmieIxSKuS2

Kelompok 5 :

1. Chikal Lyra Saeni P
2. Candra Edmond S
3. Tania Setia P

Dataset : Synthetic Crab Age Dataset
https://www.kaggle.com/datasets/iqmansingh/synthetic-crab-age-dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn import preprocessing #untuk preprosesing data
from sklearn.model_selection import train_test_split # Validasi, Split Validation
from sklearn.metrics import mean_squared_error #evaluasi MSE
from sklearn.metrics import mean_absolute_error #evaluasi MEA
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression #algoritma Linear Regression
from sklearn.ensemble import RandomForestRegressor #algoritma Random Forest
from sklearn.neighbors import KNeighborsRegressor #algoritma KNN

sns.set_theme(color_codes=True)

data = pd.read_csv('/content/syn_crab_data.csv')

data

"""Optimasi Data"""

data.head()

data.describe()

print(data.dtypes)

#cek apakah data ada yang null

data.isnull().sum()

#mengubah atribut sex menjadi nilai  yang valid
sexVals = data['Sex'].unique()

for i in sexVals:
    if(i=="M" or i=="F" or i=="I"):
        continue
    else:
        count = (data['Sex'] == i).sum()
        data['Sex'].replace(to_replace=i, method='ffill',inplace=True)
        print(f'Count of {i} in Column Sex was: ', count)

#menggabungkan data sex yang sudah diubah ke data frame
dummy = []
col = ['Sex']
for i in col:
    dummy.append(pd.get_dummies(data[i]))
crab_dummy = pd.concat(dummy, axis=1)
data = pd.concat((data,crab_dummy), axis=1)

data.drop(col,axis=1,inplace=True)
data.head()

#cek panjang, diameter dan tinggi kolom yang bernilai nol
for i in data.columns:
    count = (data[i] == 0).sum()
    print(i,count)

#menggati nilai-nilai yang kosong
data['Height'].replace(to_replace=0, value=np.NaN,inplace=True)
data['Length'].replace(to_replace=0, value=np.NaN,inplace=True)
data['Diameter'].replace(to_replace=0, value=np.NaN,inplace=True)
data.dropna(inplace=True)
data.info()

"""Evaluasi Data"""

#list semua kolom kecuali kolom Age(fungsinya sama seperti lis(zip()))
cols = [i for i in data.columns if i!="Age"]

#memilih atribut train dan label
X = data[cols]
y = data.iloc[:, 0]

#melatih data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Algoritma Linear Regresi

regressor = LinearRegression()
lrmodel = regressor.fit(X_train, y_train)
y_pred = lrmodel.predict(X_test)
mselr = mean_squared_error(y_test, y_pred)
rmselr = np.sqrt(mselr)
lrmae = mean_absolute_error(y_test, lrmodel.predict(X_test))
print("Mean Squared Error:", mselr)
print ("RMSE: ", rmselr)
print("MEA: ", lrmae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
rf1 = RandomForestRegressor()
rf1.fit(X_train, y_train)
y_pred = rf1.predict(X_test)
rf1mse = mean_squared_error(y_test, y_pred)
rf1rmse = np.sqrt(rf1mse)
rf1mae = mean_absolute_error(y_test, rf1.predict(X_test))
print("Mean Squared Error:", rf1mse)
print ("RMSE: ", rf1rmse)
print("MEA:", rf1mae)

#Algoritma Random Forest
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
rfmse = mean_squared_error(y_test, y_pred)
rfrmse = np.sqrt(rfmse)
rfmae = mean_absolute_error(y_test, rf.predict(X_test))
print("Mean Squared Error:", rfmse)
print ("RMSE: ", rfrmse)
print("MEA:", rfmae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
rf3 = RandomForestRegressor()
rf3.fit(X_train, y_train)
y_pred = rf3.predict(X_test)
rf3mse = mean_squared_error(y_test, y_pred)
rf3rmse = np.sqrt(rf3mse)
rf3mae = mean_absolute_error(y_test, rf3.predict(X_test))
print("Mean Squared Error:", rf3mse)
print ("RMSE: ", rf3rmse)
print("MEA:", rf3mae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
rf4 = RandomForestRegressor()
rf4.fit(X_train, y_train)
y_pred = rf4.predict(X_test)
rf4mse = mean_squared_error(y_test, y_pred)
rf4rmse = np.sqrt(rf4mse)
rf4mae = mean_absolute_error(y_test, rf4.predict(X_test))
print("Mean Squared Error:", rf4mse)
print ("RMSE: ", rf4rmse)
print("MEA:", rf4mae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
rf5 = RandomForestRegressor()
rf5.fit(X_train, y_train)
y_pred = rf5.predict(X_test)
rf5mse = mean_squared_error(y_test, y_pred)
rf5rmse = np.sqrt(rf5mse)
rf5mae = mean_absolute_error(y_test, rf5.predict(X_test))
print("Mean Squared Error:", rf5mse)
print ("RMSE: ", rf5rmse)
print("MEA:", rf5mae)

#Algoritma KNN
knn = KNeighborsRegressor(n_neighbors=40)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
knnmse = mean_squared_error(y_test, y_pred)
knnrmse = np.sqrt(knnmse)
knnmae = mean_absolute_error(y_test, knn.predict(X_test))
print("Mean Squared Error:", knnmse)
print ("RMSE: ", knnrmse)
print("MEA: ", knnmae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
knn5 = KNeighborsRegressor(n_neighbors=40)
knn5.fit(X_train, y_train)
y_pred = knn5.predict(X_test)
knn5mse = mean_squared_error(y_test, y_pred)
knn5rmse = np.sqrt(knn5mse)
knn5mae = mean_absolute_error(y_test, knn5.predict(X_test))
print("Mean Squared Error:", knn5mse)
print ("RMSE: ", knn5rmse)
print("MEA: ", knn5mae)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lr1 = LinearRegression()
lr1.fit(X_train, y_train)
y_pred = lr1.predict(X_test)
lr1mse = mean_squared_error(y_test, y_pred)
lr1rmse = np.sqrt(lr1mse)
lr1mae = mean_absolute_error(y_test, lr1.predict(X_test))
print("Mean Squared Error:", lr1mse)
print ("RMSE: ", lr1rmse)
print("MEA: ", lr1mae)

#grafik perbandingan MSE algoritma
algorithms = ['LR', 'RF', 'KNN']
scores = [1.1, 1.0, 4.1]

# Membuat grafik bar
plt.bar(algorithms, scores)
plt.xlabel('Algoritma')
plt.ylabel('Skor')
plt.title('Perbandingan Kinerja MSE antar Algoritma')
plt.bar(algorithms, scores, color = "#8294C4")
plt.show()

#grafik perbandingan RMSE algoritma
algorithms = ['LR', 'RF', 'KNN']
scores = [1.0, 1.0, 2.0]

# Membuat grafik bar
plt.bar(algorithms, scores)
plt.xlabel('Algoritma')
plt.ylabel('Skor')
plt.title('Perbandingan Kinerja RMSE antar Algoritma')
plt.bar(algorithms, scores, color = "#ACB1D6")
plt.show()

#grafik perbandingan MEA algoritma
algorithms = ['LR', 'RF', 'KNN']
scores = [8.5, 0.8, 1.5]

# Membuat grafik bar
plt.bar(algorithms, scores)
plt.xlabel('Algoritma')
plt.ylabel('Skor')
plt.title('Perbandingan Kinerja MEA antar Algoritma')
plt.bar(algorithms, scores, color = "#ACBCFF")
plt.show()

barWidth = 0.25

# set heights of bars
bars1 = [1.12, 1.10, 1.33, 1.31, 1.02]
bars2 = [1.06, 1.05, 3.65, 3.62, 3.19]
bars3 = [8.65, 8.58, 2.52, 2.49, 2.39]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#8E9775', width=barWidth, edgecolor='white', label='MSE')
plt.bar(r2, bars2, color='#4A503D', width=barWidth, edgecolor='white', label='RMSE')
plt.bar(r3, bars3, color='#E28F83', width=barWidth, edgecolor='white', label='MEA')

# Add xticks on the middle of the group bars
plt.xlabel('Algoritma', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['0.1', '0.2', '0.3', '0.4', '0.5'])

# Create legend & Show graphic
plt.title('Perbandingan Kinerja Algoritma Linear Regression')
plt.legend()
plt.show()

#grafik kotak perbandingan seluruh validasi

scores_lr = [1.1, 1.0, 8.5]
scores_rf = [1.0, 1.0, 0.8]
scores_knn = [4.1, 2.0, 1.5]

# Menggabungkan data skor dari setiap algoritma
data = {
    'Algoritma': ['LR'] * len(scores_lr) + ['RF'] * len(scores_rf) + ['KNN'] * len(scores_knn),
    'Skor': scores_lr + scores_rf + scores_knn
}

# Membuat grafik kotak
sns.boxplot(x='Algoritma', y='Skor', data=data)
plt.xlabel('Algoritma')
plt.ylabel('Skor')
plt.title('Perbandingan Kinerja Algoritma')
plt.show()

N = 5
mse = (1.12, 1.10, 1.33, 1.31, 1.02)
rmse = (1.06, 1.05, 3.65, 3.62, 3.19)
mae = (8.65, 8.58, 2.52, 2.49, 2.39)
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, mse, width, color='r')
ax.bar(ind, rmse, width, color='b')
ax.bar(ind, mae, width,bottom=mse, color='y')
ax.set_ylabel('Skors')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('0.1', '0.2', '0.3', '0.4', '0.5'))
ax.set_yticks(np.arange(0, 5, 9))
ax.legend(labels=['MSE', 'RMSE', 'MAE'])
plt.title('Perbandingan Kinerja Algoritma LR')
plt.show()

# Data skor untuk setiap algoritma
algorithms = ['LR', 'RF', 'KNN']
scores_lr = [7.962, 8.923, 6.365]
scores_rf = [0.993, 0.923, 0.802]
scores_knn = [6.634, 2.575, 2.002]

# Nilai parameter (opsional)
parameters = [10, 20, 30]

# Membuat grafik garis
plt.plot(parameters, scores_lr, label='LR')
plt.plot(parameters, scores_rf, label='RF')
plt.plot(parameters, scores_knn, label='KNN')

# Menambahkan label sumbu x dan y, serta judul
plt.xlabel('Parameter')
plt.ylabel('Skor')
plt.title('Perbandingan Kinerja Algoritma')

# Menambahkan legenda
plt.legend()

# Menampilkan grafik
plt.show()