def fill_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid
if __name__ == '__main__':
    rows = 3
    cols = 4
    result = fill_grid(rows, cols)
    print(result)