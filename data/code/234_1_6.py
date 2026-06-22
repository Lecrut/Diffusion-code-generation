import numpy as np

def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def create_checkerboard(size):
    validate_size(size)
    indices = np.arange(size)
    return (indices[:, None] + indices) % 2 == 0

if __name__ == '__main__':
    sample_size = 8
    checkerboard = create_checkerboard(sample_size)
    print(checkerboard)