def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)
if __name__ == '__main__':
    print(calculate_perimeter(10, 5))
    try:
        calculate_perimeter(-10, 5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_perimeter(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")