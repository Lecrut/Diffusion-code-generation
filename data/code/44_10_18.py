RECTANGLE_LENGTH = 9
RECTANGLE_WIDTH = 5

def compute_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = compute_perimeter(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    print(perimeter)