import numpy as np

def create_upper_triangular_mask(size):
    mask = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(i, size):
            mask[i, j] = 1
    return mask

if __name__ == '__main__':
    sample_size = 8
    mask = create_upper_triangular_mask(sample_size)
    print(mask)