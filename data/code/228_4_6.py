import numpy as np

def create_triangular_mask(n):
    return np.tri(n, dtype=int)

if __name__ == '__main__':
    mask = create_triangular_mask(5)
    print(mask)