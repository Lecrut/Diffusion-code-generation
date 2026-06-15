def calculate_rectangle_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
    except ValueError:
        raise TypeError("Length and width must be numeric values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    print(calculate_rectangle_perimeter(10, 5))
    try:
        calculate_rectangle_perimeter(10, "five")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_perimeter(-10, 5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_rectangle_perimeter("ten", 5)
    except TypeError as e:
        print(f"Error caught: {e}")