import numpy as np

def triangular_mask(n):
    mask = np.ones((n, n))
    np.fill_diagonal(mask, 0)
    return mask.astype(int)

if __name__ == '__main__':
    print(triangular_mask(5))