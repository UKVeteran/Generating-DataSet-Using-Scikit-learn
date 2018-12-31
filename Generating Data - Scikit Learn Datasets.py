from sklearn import datasets
from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
 
digits = datasets.load_digits()
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[8], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
