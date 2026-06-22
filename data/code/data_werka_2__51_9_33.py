RECTANGLE_LENGTH = 6
RECTANGLE_WIDTH = 4

def perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    print(perimeter(RECTANGLE_LENGTH, RECTANGLE_WIDTH))