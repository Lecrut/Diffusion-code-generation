def fill_grid():
    return [['#' for _ in range(8)] for _ in range(8)]

if __name__ == '__main__':
    grid = fill_grid()
    print(grid)