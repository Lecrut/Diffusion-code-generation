def fill_grid(rows, cols, pattern):
    return [[pattern for _ in range(cols)] for _ in range(rows)]

if __name__ == '__main__':
    grid = fill_grid(3, 4, '*')
    print(grid)