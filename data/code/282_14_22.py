def validate_input(input_string):
    if not input_string.strip():
        return False
    for item in input_string.split(','):
        if not item.strip().replace('.', '', 1).isdigit():
            return False
    return True

def calculate_sum(input_string):
    numbers = [float(item.strip()) for item in input_string.split(',')]
    total = sum(numbers)
    return total

if __name__ == '__main__':
    sample_input = "10,25.5,3,42"
    if validate_input(sample_input):
        result = calculate_sum(sample_input)
        print(result)
    else:
        print("Error: Invalid input. Please ensure all entries are valid numbers.")