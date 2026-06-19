def calculate_perimeter(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(9, 2)
        print(perimeter)
    except ValueError as e:
        print(e)