import numpy as np
GRID_SIZE = 5

def create_square_grid(size=GRID_SIZE):
    return np.array([[i % 2 for i in range(size)] for _ in range(size)])
if __name__ == '__main__':
    grid = create_square_grid()
    print(grid)