def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative values.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    print(f"Perimeter of a valid rectangle (5, 10): {calculate_rectangle_perimeter(5, 10)}")
    try:
        calculate_rectangle_perimeter(5, "ten")
    except TypeError as e:
        print(f"Error caught for invalid type: {e}")
    try:
        calculate_rectangle_perimeter(-2, 5)
    except ValueError as e:
        print(f"Error caught for negative input: {e}")