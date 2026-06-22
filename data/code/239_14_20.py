def calculate_rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        width = 5
        height = 3
        perimeter = calculate_rectangle_perimeter(width, height)
        print(perimeter)
    except ValueError as e:
        print(e)