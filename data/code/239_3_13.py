def calculate_rectangle_perimeter(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        perimeter = calculate_rectangle_perimeter(10, 5)
        print(perimeter)
    except ValueError as e:
        print(e)