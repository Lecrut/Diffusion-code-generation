def calculate_sum(input_string):
    try:
        numbers = [int(x.strip()) for x in input_string.split(',')]
        return sum(numbers)
    except ValueError:
        raise ValueError("Error: Invalid input. Please ensure all entries are valid integers.")

if __name__ == '__main__':
    sample_input = "10,25,3,40"
    try:
        result = calculate_sum(sample_input)
        print(result)
    except ValueError as e:
        print(e)