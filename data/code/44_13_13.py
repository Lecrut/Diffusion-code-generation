def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    LENGTH = 8
    WIDTH = 3
    perimeter = calculate_perimeter(LENGTH, WIDTH)
    print(perimeter)