import sys
def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        return None
    return 2 * (length + width)
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 2:
            length = float(input_data[0])
            width = float(input_data[1])
            result = calculate_perimeter(length, width)
            if result is not None:
                print(f"{result:.2f}")
        else:
            print("Insufficient input provided.")
    except ValueError:
        print("Error: Invalid numeric input provided.")
    except Exception:
        print("An unexpected error occurred.")