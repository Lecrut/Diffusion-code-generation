def calculate_sum(input_string):
    numbers = input_string.split()
    total = 0
    for item in numbers:
        try:
            total += int(item)
        except ValueError:
            return "Error: Invalid input. Please ensure all parts are valid integers."
    return total

if __name__ == '__main__':
    sample_input = "5 10 15 20"
    result = calculate_sum(sample_input)
    print(result)