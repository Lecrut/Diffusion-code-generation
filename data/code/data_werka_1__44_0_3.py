def validate_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Length and width must be positive integers.")

def calculate_rectangle_perimeter(length, width):
    validate_positive_integer(length)
    validate_positive_integer(width)
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 8
    sample_width = 4
    try:
        perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)