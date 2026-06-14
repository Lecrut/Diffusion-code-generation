import sys
def add_integers():
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            raise ValueError("Not enough input provided.")
        num1 = int(input_data[0])
        num2 = int(input_data[1])
        print(num1 + num2)
    except ValueError as e:
        print(f"Error: Invalid input. Please provide two integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    num1 = 10
    num2 = 25
    print(num1 + num2)