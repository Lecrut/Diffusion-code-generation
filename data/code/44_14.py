import sys
if __name__ == '__main__':
    try:
        data = sys.stdin.read().split()
        if len(data) >= 2:
            length = float(data[0])
            width = float(data[1])
            perimeter = 2 * (length + width)
            print(f"{perimeter:.2f}")
        else:
            print("Error: Insufficient input provided.")
    except ValueError:
        print("Error: Invalid input. Please provide two numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")