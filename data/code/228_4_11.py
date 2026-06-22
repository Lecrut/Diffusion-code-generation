import numpy as np

TRIANGULAR_MASK_N = 5

def create_triangular_mask(n=TRIANGULAR_MASK_N):
    return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    mask = create_triangular_mask()
    print(mask)