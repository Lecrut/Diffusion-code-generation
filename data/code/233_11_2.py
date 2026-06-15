def fill_rectangle(width, height, symbol):
    rectangle = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(symbol)
        rectangle.append(row)
    return rectangle
if __name__ == '__main__':
    width_val = 5
    height_val = 3
    symbol_val = '*'
    result = fill_rectangle(width_val, height_val, symbol_val)
    print(result)