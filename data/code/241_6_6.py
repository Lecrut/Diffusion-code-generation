def validate_dimensions(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Length and width must be numbers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")

def calculate_area_rectangle(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    length = 10
    width = 5
    area = calculate_area_rectangle(length, width)
    print(area)