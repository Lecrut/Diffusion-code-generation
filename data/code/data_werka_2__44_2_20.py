RECTANGLE_LENGTH = 15
RECTANGLE_WIDTH = 8

def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    print(perimeter)