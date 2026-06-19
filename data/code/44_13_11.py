def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    LENGTH = 8
    WIDTH = 4
    perimeter = calculate_perimeter(LENGTH, WIDTH)
    print(perimeter)