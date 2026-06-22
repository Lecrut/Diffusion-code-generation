def validate_and_extract_boundaries(raw_input_string):
    if not raw_input_string or not raw_input_string.strip():
        raise ValueError("Input string cannot be empty")
    tokens = raw_input_string.strip().split()
    if not tokens:
        raise ValueError("No numbers provided in input")
    parsed_numbers = []
    for token in tokens:
        try:
            value = int(token)
            parsed_numbers.append(value)
        except ValueError:
            raise ValueError(f"Invalid number format: {token}")
    if len(parsed_numbers) == 0:
        raise ValueError("Parsed list is empty")
    return parsed_numbers

def get_boundary_values(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    first_value = numbers[0]
    last_value = numbers[-1]
    return first_value, last_value

if __name__ == '__main__':
    sample_data = "100 200 300 400 500"
    number_list = validate_and_extract_boundaries(sample_data)
    first, last = get_boundary_values(number_list)
    print(first, last)