import sys
def reverse_integers():
    try:
        line = sys.stdin.read().strip()
        if not line:
            a = 10
            b = 20
        else:
            parts = line.split()
            if len(parts) < 2:
                a = 10
                b = 20
            else:
                a = int(parts[0])
                b = int(parts[1])
        reversed_result = (b, a)
        print(f"Original numbers: {a}, {b}")
        print(f"Reversed order: {reversed_result[0]}, {reversed_result[1]}")
    except ValueError:
        print("Error: Input must be valid integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    reverse_integers()