import numpy as np

def create_checkerboard(size):
    if size < 1:
        raise ValueError("Size must be a positive integer")
    
    return (np.arange(size)[:, None] + np.arange(size)) % 2 == 0

if __name__ == '__main__':
    sample_size = 8
    checkerboard = create_checkerboard(sample_size)
    print(checkerboard)