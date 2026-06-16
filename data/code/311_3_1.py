import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    try:
        numbers = list(map(int, input_data.split()))
        reversed_numbers = numbers[::-1]
        for num in reversed_numbers:
            print(num)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)