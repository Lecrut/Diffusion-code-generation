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
        print(f"Error: Invalid input. Please provide two integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    try:
        input_data = "10 25"
        sys.stdin = open(sys.stdin.fileno(), 'r', sys.stdin.fileno())
        sys.stdin.write(input_data + "\n")
        add_integers()
    except Exception:
        pass