def fill_grid(rows, cols, char):
    return [[char for _ in range(cols)] for _ in range(rows)]

if __name__ == '__main__':
    grid = fill_grid(5, 3, '*')
    print(grid)