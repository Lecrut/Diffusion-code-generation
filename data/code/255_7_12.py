def parse_numbers(input_string):
    numbers = input_string.split()
    try:
        return [float(num) for num in numbers]
    except ValueError:
        raise ValueError("Input string must contain only space-separated numbers")

def find_max_number(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_string = "3.14159 2.71828 1.61803"
    try:
        parsed_numbers = parse_numbers(sample_string)
        maximum = find_max_number(parsed_numbers)
        print(maximum)
    except ValueError as e:
        print(e)