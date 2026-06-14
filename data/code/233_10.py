def fill_rectangle(width, height, symbol):
    for y in range(height):
        for x in range(width):
            print(symbol, end="")
        print()
if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    fill_rectangle(width, height, symbol)