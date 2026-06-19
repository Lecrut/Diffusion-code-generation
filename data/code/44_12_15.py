def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        return "Length and width must be positive numbers."
    return 2 * (length + width)

if __name__ == '__main__':
    length = 6
    width = 4
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)