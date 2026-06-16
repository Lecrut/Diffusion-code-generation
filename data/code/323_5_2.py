import sys
def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            raise ValueError("Not enough input provided.")
        num1 = float(input_data[0])
        num2 = float(input_data[1])
        result = calculate_difference(num1, num2)
        print(result)
    except ValueError as e:
        print(f"Error processing input: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)