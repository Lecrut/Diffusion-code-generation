import numpy as np

def generate_triangular_mask(n):
    return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    mask = generate_triangular_mask(5)
    print(mask)