def validate_dimensions(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Width and height must be numbers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")

def calculate_rectangle_perimeter(width, height):
    validate_dimensions(width, height)
    return 2 * (width + height)

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(5, 3))