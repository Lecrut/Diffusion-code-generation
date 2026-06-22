def fill_rectangle(width, height, symbol):
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    rectangle = fill_rectangle(width, height, symbol)
    for row in rectangle:
        print(row)