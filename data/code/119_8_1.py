import sys
def reverse_integers():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        parts = line.split()
        if len(parts) != 2:
            return
        num1 = int(parts[0])
        num2 = int(parts[1])
        reversed_result = f"{num2} {num1}"
        print(reversed_result)
    except ValueError:
        print("Error: Invalid input. Please provide two integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    try:
        a = 123
        b = 456
        reversed_result = f"{b} {a}"
        print(reversed_result)
    except Exception as e:
        pass