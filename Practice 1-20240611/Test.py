import pandas as pd
import numpy as np

# using pandas to read the data for csv file
file = pd.read_csv('Advertising.csv')

# using numpy to create 3 array corresponding to 3 providing products and sales information
TV = np.array(file["TV"])
radio = np.array(file["radio"])
newspaper = np.array(file["newspaper"])
sales = np.array(file['sales'])

# create a big matrix representing the values of all products
x_train = np.array([TV, radio, newspaper])
# create a matrix representing sales value for all products
y_train = np.array([sales])
# printing x and y at the moment will resolve in a row matrix
# print(x_train, y_train)

# using transpose to have all the values present in horizontal
x_train = x_train.transpose()
y_train = y_train.transpose()

cost = 0
m = 3
for i in range(m):
  h = np.dot(x_train[i], 1) + i
  
  cost = cost + (h - y_train[i])
  print(f"Cost: {cost}")
  
  




