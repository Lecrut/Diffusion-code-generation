import numpy as np

def create_triangular_mask(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    mask = create_triangular_mask(5)
    print(mask)