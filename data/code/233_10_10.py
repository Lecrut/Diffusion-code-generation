def fill_grid(width, height, char):
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    grid = fill_grid(5, 3, '*')
    for row in grid:
        print(''.join(row))