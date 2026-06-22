def validate_dimensions(length, width):
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")

def calculate_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    length = 9
    width = 3
    try:
        perimeter = calculate_perimeter(length, width)
        print(perimeter)
    except ValueError as e:
        print(e)