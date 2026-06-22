def _validate_dimensions(dim):
    return dim > 0

def calculate_rectangle_area(width, height):
    if not _validate_dimensions(width) or not _validate_dimensions(height):
        raise ValueError("Dimensions must be positive")
    return width * height

if __name__ == '__main__':
    SAMPLE_WIDTH = 12
    SAMPLE_HEIGHT = 7
    print(calculate_rectangle_area(SAMPLE_WIDTH, SAMPLE_HEIGHT))