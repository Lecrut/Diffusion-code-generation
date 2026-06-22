import numpy as np

def create_upper_triangular_mask(n):
    return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    sample_size = 5
    mask = create_upper_triangular_mask(sample_size)
    print(mask)