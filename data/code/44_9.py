import sys
def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both dimensions must be numeric.")
    return 2 * (length + width)
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
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for dimensions.")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")