def fill_rectangle(size=8):
    return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    grid = fill_rectangle()
    print(grid)