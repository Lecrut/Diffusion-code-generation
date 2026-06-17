def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    try:
        result1 = calculate_rectangle_perimeter(10, 5)
        print(f"Perimeter for length=10, width=5: {result1}")
        result2 = calculate_rectangle_perimeter(7.5, 3)
        print(f"Perimeter for length=7.5, width=3: {result2}")
        result3 = calculate_rectangle_perimeter(-4, 6)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")
    try:
        result4 = calculate_rectangle_perimeter("a", 5)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")
    try:
        result5 = calculate_rectangle_perimeter(10, -5)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")