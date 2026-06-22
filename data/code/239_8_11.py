def calculate_rectangle_perimeter(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Width and height must be numbers.")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        perimeter = calculate_rectangle_perimeter(5, 3)
        print(perimeter)
    except ValueError as e:
        print(e)