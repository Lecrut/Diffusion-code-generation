import numpy as np
def fill_grid(coords, values):
    if not coords:
        return None
    min_r = min(c[0] for c in coords)
    max_r = max(c[0] for c in coords)
    min_c = min(c[1] for c in coords)
    max_c = max(c[1] for c in coords)
    rows = max_r - min_r + 1
    cols = max_c - min_c + 1
    grid = np.zeros((rows, cols), dtype=int)
    for (r, c), val in zip(coords, values):
        grid[r - min_r, c - min_c] = val
    return grid
if __name__ == '__main__':
    sample_coords = [(1, 3), (5, 1), (2, 4), (6, 2)]
    sample_values = [10, 20, 30, 40]
    result_grid = fill_grid(sample_coords, sample_values)
    print(result_grid)