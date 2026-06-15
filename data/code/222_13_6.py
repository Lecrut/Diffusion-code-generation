import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    input_data = "10 5 -3 22 8"
    try:
        numbers = input_data.split()
        numeric_list = []
        for item in numbers:
            if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                numeric_list.append(int(item))
            else:
                raise ValueError(f"Invalid non-numeric input found: {item}")
        if not numeric_list:
            raise ValueError("No valid numbers were extracted from the input.")
        minimum_value = find_minimum(numeric_list)
        print(minimum_value)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)