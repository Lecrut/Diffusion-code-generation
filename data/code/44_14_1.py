import sys
def calculate_perimeter(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        perimeter = 2 * (length + width)
        return f"{perimeter:.2f}"
    else:
        return "Error: Invalid numeric input"
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 2:
            length = float(input_data[0])
            width = float(input_data[1])
            print(calculate_perimeter(length, width))
        else:
            print("Error: Insufficient input provided.")
    except ValueError:
        print("Error: One or both inputs were not valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")