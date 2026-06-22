import numpy as np

def create_square_grid(size):
    return np.array([[i % 2 for i in range(size)] for _ in range(size)])

if __name__ == '__main__':
    grid = create_square_grid(5)
    print(grid)