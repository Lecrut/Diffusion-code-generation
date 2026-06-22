def calculate_sum(input_string):
    numbers = []
    for item in input_string.split(','):
        if item.strip():
            try:
                numbers.append(int(item.strip()))
            except ValueError:
                return "Error: Invalid input. Please ensure all entries are valid integers."
    total = sum(numbers)
    return total

if __name__ == '__main__':
    sample_input = "10, 25, 30, 40"
    result = calculate_sum(sample_input)
    print(result)