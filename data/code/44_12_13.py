LENGTH = 12
WIDTH = 6

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = calculate_rectangle_perimeter(LENGTH, WIDTH)
    print(perimeter)