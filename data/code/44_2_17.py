def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    LENGTH = 18
    WIDTH = 7
    perimeter = calculate_perimeter(LENGTH, WIDTH)
    print(perimeter)