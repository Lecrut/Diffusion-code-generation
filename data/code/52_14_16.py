def validate_rectangle_params(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")

def calculate_area(length, width):
    validate_rectangle_params(length, width)
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    area = calculate_area(sample_length, sample_width)
    print(area)