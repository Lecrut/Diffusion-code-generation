import numpy as np

def create_hollow_square_grid(size, border_value=1, interior_value=0):
    if size <= 0:
        return np.array([])
    if size == 1:
        return np.full((1, 1), border_value, dtype=int)
    grid = np.full((size, size), interior_value, dtype=int)
    grid[0, :] = border_value
    grid[-1, :] = border_value
    grid[:, 0] = border_value
    grid[:, -1] = border_value
    return grid

if __name__ == '__main__':
    sample_size = 5
    result = create_hollow_square_grid(sample_size)
    print(result)