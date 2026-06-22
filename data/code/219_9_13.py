def parse_csv_string(csv_str):
    try:
        return [int(num) for num in csv_str.split(',')]
    except ValueError as e:
        raise ValueError("Invalid CSV string") from e

def find_maximum_value(numbers):
    if not numbers:
        raise ValueError("No values provided")
    return max(numbers)

if __name__ == '__main__':
    csv_input = "10,5,20,3"
    try:
        parsed_numbers = parse_csv_string(csv_input)
        result = find_maximum_value(parsed_numbers)
        print(result)
    except ValueError as e:
        print(e)