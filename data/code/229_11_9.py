import numpy as np

def generate_square_grid(n):
    if n <= 0:
        raise ValueError("Grid size must be greater than zero")
    
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            grid[i, j] = (i + j) % 2
    return grid

if __name__ == '__main__':
    try:
        grid = generate_square_grid(5)
        print(grid)
    except ValueError as e:
        print(e)