import numpy as np

TRIANGULAR_MASK_K = 0

def triangular_mask(n):
    return np.triu(np.ones((n, n)), k=TRIANGULAR_MASK_K)

if __name__ == '__main__':
    print(triangular_mask(5))