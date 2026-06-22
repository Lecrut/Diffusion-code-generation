def calculate_rectangle_perimeter(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric values.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return 2 * (width + height)

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(10, 5))
    try:
        calculate_rectangle_perimeter(10, "five")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_perimeter(-2, 5)
    except ValueError as e:
        print(f"Error caught: {e}")