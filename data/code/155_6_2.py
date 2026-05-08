def calculate_sum(input_string):
    try:
        numbers = input_string.split()
        total = 0
        for num_str in numbers:
            total += int(num_str)
        return total
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are valid integers."
if __name__ == '__main__':
    sample_input = "10 20 30 40"
    result = calculate_sum(sample_input)
    print(result)