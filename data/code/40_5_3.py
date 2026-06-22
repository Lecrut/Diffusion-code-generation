BOX_LENGTH = 10
BOX_WIDTH = 8
BOX_HEIGHT = 6

def validate_dimension(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def calculate_surface_area(length, width, height):
    validate_dimension(length, "length")
    validate_dimension(width, "width")
    validate_dimension(height, "height")
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    print(calculate_surface_area(BOX_LENGTH, BOX_WIDTH, BOX_HEIGHT))