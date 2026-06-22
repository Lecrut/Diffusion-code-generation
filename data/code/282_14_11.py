def calculate_sum(input_string):
    numbers = []
    for item in input_string.split(','):
        try:
            number = float(item.strip())
            numbers.append(number)
        except ValueError:
            continue
    return sum(numbers)
if __name__ == '__main__':
    sample_input = '10, 25.5, 3, 42'
    result = calculate_sum(sample_input)
    print(result)