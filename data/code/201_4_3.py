def calculate_average(data_string):
    numbers = []
    for item in data_string.split(','):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            return None
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_input = "10,20,30,40,error"
    average = calculate_average(sample_input)
    print(average)
    sample_input_valid = "5.5,10,15.5,20"
    average_valid = calculate_average(sample_input_valid)
    print(average_valid)
    sample_input_empty = ""
    average_empty = calculate_average(sample_input_empty)
    print(average_empty)
    sample_input_only_text = "a,b,c"
    average_text = calculate_average(sample_input_only_text)
    print(average_text)