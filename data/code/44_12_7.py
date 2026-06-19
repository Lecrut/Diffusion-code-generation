def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        perimeter = calculate_rectangle_perimeter(9, 6)
        print(perimeter)
    except ValueError as e:
        print(e)