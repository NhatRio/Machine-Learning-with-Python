# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values #Make sure that X is a matrix
y = dataset.iloc[:, 2].values

#Splitting the dataset into the Training set and the Test set 
'''from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


#Fitting Linear Regression to the data set
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y) 


#Fitting Polynomial Regression to the data set
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)#polynomial degree
X_poly = poly_reg.fit_transform(X) #X_poly is the transform matrix of X with the features(columns) x1 and x1^2
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)                                    



#Visualising the Linear Regression results
plt.scatter(X, y, color = 'red') #real values
plt.plot(X, lin_reg.predict(X), color = 'blue') # preditive values
plt.title('Truth or Bluff( Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



#Visualising the Polynominal Regression results
#X_grid = np.arange(min(X),max(X), 0.1) #create a vector X_grid to make the curve smoother
#X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red') #real values
#plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') # preditive values
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue') # preditive values
plt.title('Truth or Bluff( Polynominal Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


#Predicting a result with Linear Regression
lin_reg.predict(6.5)


#Predicting a result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))
