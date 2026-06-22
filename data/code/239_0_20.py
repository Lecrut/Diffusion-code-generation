def calculate_perimeter(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Width and height must be numbers")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        width = 5
        height = 3
        perimeter = calculate_perimeter(width, height)
        print(perimeter)
    except ValueError as e:
        print(e)