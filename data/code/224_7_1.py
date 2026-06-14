def calculate_mean(input_string):
    numbers = []
    try:
        parts = input_string.split()
        for part in parts:
            numbers.append(float(part))
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    except ValueError:
        return "Error: Invalid number found"
if __name__ == '__main__':
    sample_input = "10 20 30 40"
    result = calculate_mean(sample_input)
    print(result)
    sample_input_error = "10 20 hello 40"
    result_error = calculate_mean(sample_input_error)
    print(result_error)
    sample_input_empty = ""
    result_empty = calculate_mean(sample_input_empty)
    print(result_empty)
    sample_input_only_text = "abc def"
    result_text = calculate_mean(sample_input_only_text)
    print(result_text)