import numpy as np

def generate_upper_triangular_mask(size):
    return np.triu(np.ones((size, size)), k=0)

if __name__ == '__main__':
    sample_size = 7
    mask = generate_upper_triangular_mask(sample_size)
    print(mask)