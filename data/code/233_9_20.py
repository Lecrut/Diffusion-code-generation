def create_filled_rectangle(width=8, height=8):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    return [['#' for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    filled_grid = create_filled_rectangle(sample_width, sample_height)
    print(filled_grid)