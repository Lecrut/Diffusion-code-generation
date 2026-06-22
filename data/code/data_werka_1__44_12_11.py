def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 15
        width = 6
        perimeter = calculate_rectangle_perimeter(length, width)
        print(perimeter)
    except ValueError as e:
        print(e)