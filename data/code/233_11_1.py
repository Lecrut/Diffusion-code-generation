def fill_rectangle(width, height, symbol):
    grid = []
    for _ in range(height):
        row = [symbol] * width
        grid.append(row)
    return grid
if __name__ == '__main__':
    width_val = 5
    height_val = 3
    symbol_val = '#'
    result = fill_rectangle(width_val, height_val, symbol_val)
    print(result)