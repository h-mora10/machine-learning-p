import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Importing the dataset
dataset = pd.read_csv('dataset/Data.csv')
x = dataset.iloc[:, :-1].values  # Features
y = dataset.iloc[:, -1].values  # Target variable

print(x)
print(y)

# Handling missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3]) # Fit on the columns with missing values
x[:, 1:3] = imputer.transform(x[:, 1:3]) # Transform the data

print(x)

# Encoding categorical data

## Encoding the independent variable
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))  # Fit and transform the independent variable

print(x)

# Encoding the dependent variable
le = LabelEncoder()
y = le.fit_transform(y)  # Fit and transform the dependent variable

print(y)

# Splitting the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print("x_train:", x_train)
print("x_test:", x_test)
print("y_train:", y_train)
print("y_test:", y_test)

# Feature Scaling
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])  # Fit and transform the training set
x_test[:, 3:] = sc.transform(x_test[:, 3:])  # Transform the test set

print("x_train:", x_train)
print("x_test:", x_test)