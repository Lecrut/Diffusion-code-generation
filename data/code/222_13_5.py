import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list is empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    input_data = "10 5 22 3 8"
    try:
        numbers = [int(x) for x in input_data.split()]
        if not numbers:
            print("Error: No valid numbers found.")
        else:
            minimum_value = find_minimum(numbers)
            print(minimum_value)
    except ValueError as e:
        print(f"Error: Invalid input detected. Ensure all provided values are numeric. Details: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)