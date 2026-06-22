def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_rectangle_perimeter(length, width):
    validate_dimensions(length, width)
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_length = 10
    sample_width = 5
    perimeter_result = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter_result)