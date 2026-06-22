def validate_dimensions(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")

def calculate_rectangle_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 5
        width = 3
        perimeter = calculate_rectangle_perimeter(length, width)
        print(perimeter)
    except ValueError as e:
        print(e)