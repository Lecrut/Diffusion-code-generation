import sys
def calculate_sum(input_string):
    numbers = []
    for item in input_string.split(','):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            pass
    return sum(numbers)
if __name__ == '__main__':
    sample_input = "10,25,33.5,42"
    result = calculate_sum(sample_input)
    print(result)