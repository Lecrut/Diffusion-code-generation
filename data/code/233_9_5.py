def fill_rectangle():
    symbol = '#'
    size = 8
    rectangle = [[symbol for _ in range(size)] for _ in range(size)]
    return rectangle

if __name__ == '__main__':
    grid = fill_rectangle()
    print(grid)