SIZE = 8

def create_rectangle(size=SIZE):
    return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    sample_grid = create_rectangle(5)
    print(sample_grid)