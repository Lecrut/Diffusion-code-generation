def validate_dimensions(length, width):
    if not all(isinstance(x, (int, float)) for x in [length, width]):
        raise ValueError("Length and width must be numbers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")

def calculate_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    length_val = 10.5
    width_val = 5.0
    area = calculate_area(length_val, width_val)
    print(area)