def calculate_rectangle_perimeter(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    return 2 * (width + height)

if __name__ == '__main__':
    width = 5
    height = 3
    try:
        perimeter = calculate_rectangle_perimeter(width, height)
        print(perimeter)
    except ValueError as e:
        print(e)