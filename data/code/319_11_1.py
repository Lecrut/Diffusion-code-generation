def fill_grid(coords, values):
    if not coords:
        return []
    min_r = min(c[0] for c in coords)
    max_r = max(c[0] for c in coords)
    min_c = min(c[1] for c in coords)
    max_c = max(c[1] for c in coords)
    rows = max_r - min_r + 1
    cols = max_c - min_c + 1
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for (r, c), val in zip(coords, values):
        row_index = r - min_r
        col_index = c - min_c
        grid[row_index][col_index] = val
    return grid
if __name__ == '__main__':
    sample_coords = [(1, 3), (5, 1), (2, 4), (8, 7)]
    sample_values = [10, 20, 30, 40]
    result_grid = fill_grid(sample_coords, sample_values)
    for row in result_grid:
        print(row)