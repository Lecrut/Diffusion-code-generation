def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers")

def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    validate_dimensions(length, width)
    print(calculate_perimeter(length, width))