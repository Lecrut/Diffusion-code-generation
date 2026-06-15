import sys
def add_integers():
    try:
        data = sys.stdin.read().split()
        if len(data) < 2:
            raise ValueError("Not enough input provided.")
        num1 = int(data[0])
        num2 = int(data[1])
        print(num1 + num2)
    except ValueError as e:
        print(f"Error: Invalid input. Ensure both inputs are integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 25
    try:
        result = sample_num1 + sample_num2
        print(result)
    except Exception as e:
        print(f"Error during calculation: {e}", file=sys.stderr)