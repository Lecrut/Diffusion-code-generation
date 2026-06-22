import numpy as np

def create_square_grid(n):
    side_length = int(np.ceil(np.sqrt(n)))
    return np.arange(n).reshape((side_length, side_length))

if __name__ == '__main__':
    grid = create_square_grid(16)
    print(grid)