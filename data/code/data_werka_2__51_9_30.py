def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rectangle_length = 10
    rectangle_width = 6
    print(calculate_perimeter(rectangle_length, rectangle_width))