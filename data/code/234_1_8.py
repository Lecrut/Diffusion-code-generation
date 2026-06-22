import numpy as np

def create_checkerboard(size):
    row = np.array([1 if i % 2 == 0 else 0 for i in range(size)])
    checkerboard = np.tile(row, (size, 1))
    return checkerboard

if __name__ == '__main__':
    sample_size = 6
    checkerboard = create_checkerboard(sample_size)
    print(checkerboard)