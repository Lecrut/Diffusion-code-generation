import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            side_length = 5
        else:
            side_length = float(input_data)
        area = side_length * side_length
        print(area)
    except ValueError:
        print("Error: Invalid input provided.", file=sys.stderr)
    except Exception:
        print("An error occurred.", file=sys.stderr)