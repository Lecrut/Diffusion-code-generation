import numpy as np

def generate_upper_triangular_mask(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return np.triu(np.ones((n, n)))

if __name__ == '__main__':
    sample_size = 7
    mask = generate_upper_triangular_mask(sample_size)
    print(mask)