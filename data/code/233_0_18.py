def generate_asterisk_grid(width, height):
    return [['*' for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    grid_width = 5
    grid_height = 3
    asterisk_grid = generate_asterisk_grid(grid_width, grid_height)
    for row in asterisk_grid:
        print(''.join(row))