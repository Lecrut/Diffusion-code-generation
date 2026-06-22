import numpy as np

def create_grid():
    grid = np.zeros((5, 5), dtype=int)
    for i in range(5):
        for j in range(5):
            if (i + j) % 2 == 1:
                grid[i, j] = 1
    return grid

if __name__ == '__main__':
    print(create_grid())