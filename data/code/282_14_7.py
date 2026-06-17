import sys
def calculate_sum(input_string):
    numbers = []
    try:
        for item in input_string.split(','):
            if item.strip():
                numbers.append(float(item.strip()))
        return sum(numbers)
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are valid numbers."
if __name__ == '__main__':
    sample_input = "10,25,3.5,40"
    result = calculate_sum(sample_input)
    print(result)