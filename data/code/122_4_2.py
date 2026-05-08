import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = []
    try:
        for item in input_data.split():
            numbers.append(int(item))
        if not numbers:
            average = 0
        else:
            average = sum(numbers) / len(numbers)
        print(average)
    except ValueError:
        print("Error: Invalid input detected. Please ensure all inputs are numeric.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)