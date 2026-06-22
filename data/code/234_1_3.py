import numpy as np

def create_checkerboard(size):
    return (np.arange(size)[:, None] + np.arange(size)) % 2 == 0

if __name__ == '__main__':
    sample_size = 4
    checkerboard = create_checkerboard(sample_size)
    for row in checkerboard:
        print(row)