RECTANGLE_SIZE = 8

def fill_rectangle(size=RECTANGLE_SIZE):
    return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    grid = fill_rectangle()
    print(grid)