import sys
def calculate_sum(input_string):
    try:
        numbers = [float(x.strip()) for x in input_string.split(',')]
        total = sum(numbers)
        return total
    except ValueError:
        return "Error: Invalid input. Please ensure all entries are valid numbers."
if __name__ == '__main__':
    sample_input = "10, 5.5, 20, 3.5"
    result = calculate_sum(sample_input)
    print(f"Input string: {sample_input}")
    print(f"Calculated sum: {result}")