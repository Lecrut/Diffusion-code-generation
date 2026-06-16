def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)
if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(10, 5)
        print(f"Perimeter for length=10, width=5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_perimeter(-3, 4)
        print(f"Perimeter for length=-3, width=4: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = calculate_perimeter(0, 10)
        print(f"Perimeter for length=0, width=10: {result3}")
    except ValueError as e:
        print(f"Error: {e}")