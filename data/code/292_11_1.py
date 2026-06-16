def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)
if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(10, 5)
        print(f"Perimeter for length=10, width=5 is: {result1}")
        result2 = calculate_perimeter(7, 3)
        print(f"Perimeter for length=7, width=3 is: {result2}")
        result3 = calculate_perimeter(-4, 5)
    except ValueError as e:
        print(f"Error caught: {e}")