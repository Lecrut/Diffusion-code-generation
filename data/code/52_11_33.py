def validate_dimensions(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_rectangle_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    sample_length = 6.2
    sample_width = 4.8
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)