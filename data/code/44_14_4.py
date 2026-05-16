import sys
def calculate_perimeter(length, width):
    return 2 * (length + width)
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 2:
            length = float(input_data[0])
            width = float(input_data[1])
            perimeter = calculate_perimeter(length, width)
            print(f"{perimeter:.2f}")
        else:
            print("Error: Insufficient input provided.")
    except ValueError:
        print("Error: Invalid input. Please provide two numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")