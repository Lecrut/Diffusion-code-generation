def parse_numbers(input_string):
    parts = input_string.split()
    numbers = []
    for part in parts:
        try:
            numbers.append(float(part))
        except ValueError:
            return None
    return numbers

def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_input_1 = "10 20 30 40"
    parsed_numbers_1 = parse_numbers(sample_input_1)
    mean_value_1 = calculate_mean(parsed_numbers_1)
    print(f"The mean of {sample_input_1} is: {mean_value_1}")

    sample_input_2 = "5.5 10.5 15.0"
    parsed_numbers_2 = parse_numbers(sample_input_2)
    mean_value_2 = calculate_mean(parsed_numbers_2)
    print(f"The mean of {sample_input_2} is: {mean_value_2}")