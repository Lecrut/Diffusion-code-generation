def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 6
    perimeter = calculate_perimeter(sample_length, sample_width)
    print(perimeter)