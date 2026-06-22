def _validate_dimensions(dim):
    if dim <= 0:
        raise ValueError("Dimension must be positive")
    return True

def get_rectangle_area(width, height):
    _validate_dimensions(width)
    _validate_dimensions(height)
    return width * height

if __name__ == '__main__':
    WIDTH_CONSTANT = 12
    HEIGHT_CONSTANT = 7
    computed_area = get_rectangle_area(WIDTH_CONSTANT, HEIGHT_CONSTANT)
    print(computed_area)