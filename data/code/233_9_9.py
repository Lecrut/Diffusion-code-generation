def create_filled_rectangle(width=8, height=8):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")
    
    rectangle = [['#' for _ in range(width)] for _ in range(height)]
    return rectangle

if __name__ == '__main__':
    sample_width = 6
    sample_height = 4
    filled_grid = create_filled_rectangle(sample_width, sample_height)
    print(filled_grid)