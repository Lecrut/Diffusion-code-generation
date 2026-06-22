def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    L = 15
    W = 8
    perimeter = calculate_perimeter(L, W)
    print(perimeter)