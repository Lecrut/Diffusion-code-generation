def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both dimensions must be numeric.")
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        LENGTH = 8.0
        WIDTH = 4.5
        perimeter = calculate_perimeter(LENGTH, WIDTH)
        print(f"Length: {LENGTH}")
        print(f"Width: {WIDTH}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: Invalid input provided. {e}")
    except TypeError as e:
        print(f"Error: Type error. {e}")