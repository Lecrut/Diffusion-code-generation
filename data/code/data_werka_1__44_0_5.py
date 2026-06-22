def is_positive_integer(value):
    return isinstance(value, int) and value > 0

def validate_dimensions(length, width):
    if not (is_positive_integer(length) and is_positive_integer(width)):
        raise ValueError("Length and width must be positive integers.")

def calculate_rectangle_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 9
    sample_width = 5
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)