def calculate_sum(input_string):
    number_mapping = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0
    }
    
    numbers = []
    for item in input_string.split(','):
        if item.strip().lower() in number_mapping:
            numbers.append(number_mapping[item.strip().lower()])
        else:
            try:
                numbers.append(float(item.strip()))
            except ValueError:
                return "Error: Invalid input. Please ensure all entries are valid numbers."
    
    return sum(numbers)

if __name__ == '__main__':
    sample_input = "one, two, three, 4.5, five"
    result = calculate_sum(sample_input)
    print(result)