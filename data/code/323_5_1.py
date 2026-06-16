import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            num1 = 10
            num2 = 5
        else:
            num1 = int(input_data[0])
            num2 = int(input_data[1])
        result = calculate_difference(num1, num2)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)