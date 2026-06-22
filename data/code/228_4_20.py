import numpy as np

def generate_upper_triangular_mask(n):
    ones_matrix = np.ones((n, n))
    upper_triangular_mask = np.triu(ones_matrix)
    return upper_triangular_mask

if __name__ == '__main__':
    sample_size = 10
    mask = generate_upper_triangular_mask(sample_size)
    print(mask)