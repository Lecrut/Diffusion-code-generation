def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def fill_rectangle(size=8):
    validate_size(size)
    return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    sample_grid = fill_rectangle(5)
    print(sample_grid)