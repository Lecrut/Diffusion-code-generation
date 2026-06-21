MAX_FLOAT_VALUE = float('inf')

def validate_input(values):
    if not isinstance(values, list) or len(values) == 0:
        raise ValueError("Input must be a non-empty list of floats")

def calculate_mean(numbers):
    validate_input(numbers)
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    result = calculate_mean(sample_values)
    print(result)