def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, (int, float)) or length <= 0:
        raise ValueError("Length must be a positive number")
    if not isinstance(width, (int, float)) or width <= 0:
        raise ValueError("Width must be a positive number")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 10
        width = 5
        perimeter = calculate_rectangle_perimeter(length, width)
        print(f"Perimeter of rectangle: {perimeter}")
    except ValueError as e:
        print(e)