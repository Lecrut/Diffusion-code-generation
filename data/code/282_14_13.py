def parse_input(input_string):
    numbers = []
    for item in input_string.split(','):
        if item.strip():
            try:
                number = float(item.strip())
                numbers.append(number)
            except ValueError:
                raise ValueError("Invalid input. Please ensure all entries are valid numbers.")
    return numbers

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