FIXED_LENGTH = 10
FIXED_WIDTH = 6

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = FIXED_LENGTH
    width = FIXED_WIDTH
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)