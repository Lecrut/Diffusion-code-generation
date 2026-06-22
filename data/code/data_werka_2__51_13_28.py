def validate_positive_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    if value <= 0:
        raise ValueError("Value must be positive.")

def calculate_perimeter(length, width):
    validate_positive_number(length)
    validate_positive_number(width)
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 2
    try:
        perimeter = calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)