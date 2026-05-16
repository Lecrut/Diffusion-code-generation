import sys
def check_equality(num1, num2):
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            raise ValueError("Insufficient input provided.")
        num1 = float(input_data[0])
        num2 = float(input_data[1])
        check_equality(num1, num2)
    except ValueError as e:
        print(f"Error: Invalid input. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)