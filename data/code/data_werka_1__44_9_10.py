def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both dimensions must be numeric.")
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")

def calculate_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 15
        width = 7
        perimeter = calculate_perimeter(length, width)
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Perimeter: {perimeter}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")