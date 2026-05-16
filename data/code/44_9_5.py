import sys
def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        return "Error: Dimensions must be positive."
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    try:
        length_str = "10"
        width_str = "5"
        length = float(length_str)
        width = float(width_str)
        result = calculate_perimeter(length, width)
        if isinstance(result, str) and result.startswith("Error"):
            print(result)
        else:
            print(f"Length: {length}, Width: {width}")
            print(f"Perimeter: {result}")
    except ValueError:
        print("Error: Invalid input. Please ensure dimensions are numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")