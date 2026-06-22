def create_pattern(width, height, symbol):
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    grid_width = 15
    grid_height = 7
    pattern_char = "#"
    pattern = create_pattern(grid_width, grid_height, pattern_char)
    for row in pattern:
        print(row)