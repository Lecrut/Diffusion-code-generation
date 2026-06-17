def fill_grid(coords, values):
    if not coords:
        return []
    min_r = min(c[0] for c in coords)
    max_r = max(c[0] for c in coords)
    min_c = min(c[1] for c in coords)
    max_c = max(c[1] for c in coords)
    R = max_r - min_r + 1
    C = max_c - min_c + 1
    grid = [[0 for _ in range(C)] for _ in range(R)]
    for (r, c), val in zip(coords, values):
        row = r - min_r
        col = c - min_c
        grid[row][col] = val
    return grid
if __name__ == '__main__':
    sample_coords = [(0, 0), (1, 2), (3, 1)]
    sample_values = [10, 20, 30]
    result_grid = fill_grid(sample_coords, sample_values)
    print(result_grid)