def calculate_rectangle_perimeter(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Both width and height must be numbers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        print(calculate_rectangle_perimeter(5, 3))
    except ValueError as e:
        print(e)