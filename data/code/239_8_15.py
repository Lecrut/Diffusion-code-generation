def calculate_rectangle_perimeter(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Width and height must be numbers")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        perimeter = calculate_rectangle_perimeter(5, 3)
        print(perimeter)
    except ValueError as e:
        print(e)