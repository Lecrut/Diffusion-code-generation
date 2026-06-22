def parse_input(input_string):
    try:
        return [float(item.strip()) for item in input_string.split(',')]
    except ValueError:
        raise ValueError("Invalid input. Please ensure all entries are valid numbers.")

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_input = "10, 25.5, 3, 42"
    try:
        parsed_numbers = parse_input(sample_input)
        result = calculate_sum(parsed_numbers)
        print(result)
    except ValueError as e:
        print(e)