def parse_input(input_string):
    try:
        numbers = [float(num) for num in input_string.split()]
        if not numbers:
            raise ValueError("Input string cannot be empty")
        return numbers
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

def find_max_number(numbers):
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_string = "3.14159 2.71828 1.61803"
    try:
        parsed_numbers = parse_input(sample_string)
        maximum = find_max_number(parsed_numbers)
        print(maximum)
    except ValueError as e:
        print(e)