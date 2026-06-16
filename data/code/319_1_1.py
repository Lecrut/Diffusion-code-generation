def fill_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid
if __name__ == '__main__':
    rows_val = 3
    cols_val = 4
    result = fill_grid(rows_val, cols_val)
    print(result)