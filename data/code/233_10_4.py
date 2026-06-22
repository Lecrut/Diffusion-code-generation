def fill_grid(rows, cols, char):
    return [[char for _ in range(cols)] for _ in range(rows)]

if __name__ == '__main__':
    grid = fill_grid(3, 4, '*')
    for row in grid:
        print(''.join(row))