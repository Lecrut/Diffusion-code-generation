import sys
if __name__ == '__main__':
    input_data = "1 2 3 4 5"
    numbers = []
    try:
        input_numbers = input_data.split()
        for item in input_numbers:
            numbers.append(int(item))
        reversed_numbers = numbers[::-1]
        print(*(reversed_numbers))
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)