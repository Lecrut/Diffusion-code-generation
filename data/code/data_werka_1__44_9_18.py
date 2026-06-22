def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both dimensions must be numeric.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        LENGTH = 10
        WIDTH = 5
        perimeter = calculate_perimeter(LENGTH, WIDTH)
        print(f"Length: {LENGTH}")
        print(f"Width: {WIDTH}")
        print(f"Perimeter: {perimeter}")
    except TypeError as e:
        print(f"Error: Invalid input. {e}", file=sys.stderr)