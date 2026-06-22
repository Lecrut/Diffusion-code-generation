GRID_SIZE = 8

def fill_rectangle(size=GRID_SIZE):
    return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    sample_grid = fill_rectangle(5)
    print(sample_grid)