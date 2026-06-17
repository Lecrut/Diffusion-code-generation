def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative values.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    try:
        result1 = calculate_rectangle_perimeter(10, 5)
        print(f"Perimeter for length=10, width=5 is: {result1}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_rectangle_perimeter(10.5, 4)
        print(f"Perimeter for length=10.5, width=4 is: {result2}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        calculate_rectangle_perimeter(-2, 5)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        calculate_rectangle_perimeter("a", 5)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")