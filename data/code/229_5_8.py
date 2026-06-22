import numpy as np

def create_grid():
    return np.arange(16).reshape(4, 4)

if __name__ == '__main__':
    grid = create_grid()
    print(grid)