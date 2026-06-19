LENGTH = 15
WIDTH = 8

def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    perimeter = calculate_perimeter(LENGTH, WIDTH)
    print(perimeter)