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
        return None
if __name__ == '__main__':
    sample_input = "10 20 30 40"
    mean_value = calculate_mean(sample_input)
    print(f"The mean of {sample_input} is: {mean_value}")
    sample_input_error = "10 20 hello 40"
    mean_value_error = calculate_mean(sample_input_error)
    print(f"The mean of {sample_input_error} is: {mean_value_error}")
    sample_input_empty = ""
    mean_value_empty = calculate_mean(sample_input_empty)
    print(f"The mean of '{sample_input_empty}' is: {mean_value_empty}")
    sample_input_only_text = "abc def"
    mean_value_text = calculate_mean(sample_input_only_text)
    print(f"The mean of '{sample_input_only_text}' is: {mean_value_text}")