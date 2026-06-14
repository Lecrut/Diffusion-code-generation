def fill_rectangle(width, height, symbol):
    for y in range(height):
        for x in range(width):
            print(symbol, end="")
        print()
if __name__ == '__main__':
    fill_rectangle(5, 7, "#")