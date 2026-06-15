import sys
def find_minimum(data):
    if not data:
        raise ValueError("Input list is empty")
    minimum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_input = "10 5 22 3 8"
    try:
        input_data = sample_input.split()
        numeric_list = []
        for item in input_data:
            if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                numeric_list.append(int(item))
            else:
                raise ValueError(f"Invalid non-numeric input found: {item}")
        if not numeric_list:
            raise ValueError("No valid numbers were parsed from the input.")
        minimum_value = find_minimum(numeric_list)
        print(minimum_value)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)