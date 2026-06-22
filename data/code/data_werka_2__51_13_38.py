RECTANGLE_LENGTH = 10
RECTANGLE_WIDTH = 6

def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    print(perimeter)