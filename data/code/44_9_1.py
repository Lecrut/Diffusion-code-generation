import sys
def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    try:
        length_str = "10"
        width_str = "5"
        length = float(length_str)
        width = float(width_str)
        perimeter = calculate_perimeter(length, width)
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: Invalid input provided. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)