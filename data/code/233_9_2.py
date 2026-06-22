def create_rectangle(size=8):
    rectangle = [['#' for _ in range(size)] for _ in range(size)]
    return rectangle

if __name__ == '__main__':
    sample_grid = create_rectangle(5)
    print(sample_grid)