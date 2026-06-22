import numpy as np

def create_checkerboard(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    return (np.arange(size)[:, None] + np.arange(size)) % 2 == 0

if __name__ == '__main__':
    sample_size = 4
    checkerboard = create_checkerboard(sample_size)
    for row in checkerboard:
        print(row)