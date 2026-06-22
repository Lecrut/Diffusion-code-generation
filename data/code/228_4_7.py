import numpy as np

TRIANGULAR_MASK_SIZE = 5

def generate_triangular_mask(size=TRIANGULAR_MASK_SIZE):
    return np.triu(np.ones((size, size)), k=0)

if __name__ == '__main__':
    mask = generate_triangular_mask()
    print(mask)