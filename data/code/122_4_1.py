import sys
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    try:
        numbers = [int(x) for x in input_data.split()]
        average = calculate_average(numbers)
        print(average)
    except ValueError:
        print("Error: Input contains non-numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)