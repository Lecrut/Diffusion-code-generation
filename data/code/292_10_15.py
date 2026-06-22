def validate_dimensions(length, width):
    if not (isinstance(length, int) and isinstance(width, int)):
        raise ValueError("Both length and width must be integers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be greater than zero")

def calculate_rectangle_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(calculate_rectangle_perimeter(length, width))