def calculate_average(data_string):
    numbers = []
    try:
        for item in data_string.split(','):
            numbers.append(float(item.strip()))
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are valid numbers."
if __name__ == '__main__':
    sample_input = "10,20.5,30,40.5"
    average = calculate_average(sample_input)
    print(average)