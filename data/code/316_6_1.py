def print_grid():
    width = 10
    height = 5
    symbol = '#'
    for y in range(height):
        for x in range(width):
            print(symbol, end='')
        print()
if __name__ == '__main__':
    print_grid()