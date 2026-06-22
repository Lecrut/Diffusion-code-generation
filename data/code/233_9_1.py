def fill_rectangle():
    return [['#' for _ in range(8)] for _ in range(8)]

if __name__ == '__main__':
    grid = fill_rectangle()
    print(grid)