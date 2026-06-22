import numpy as np

def triangular_mask(n):
    return np.triu(np.ones((n, n)))

if __name__ == '__main__':
    print(triangular_mask(5))