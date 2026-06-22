def validate_dimensions(width, height):
    if not isinstance(width, int) or not isinstance(height, int):
        raise ValueError("Both width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Both width and height must be positive integers.")

def calculate_area(width, height):
    validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    area = calculate_area(5, 3)
    print(area)