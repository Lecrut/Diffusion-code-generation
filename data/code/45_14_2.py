import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            radius = 5.0
        else:
            radius = float(input_data)
        area = math.pi * (radius ** 2)
        print(area)
    except ValueError:
        print("Error: Invalid input. Please provide a valid number.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)