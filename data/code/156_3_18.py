MEAN_CALCULATION_ERROR = "Input must be a non-empty list of floats"

def validate_input(values):
    if not isinstance(values, list) or len(values) == 0:
        raise ValueError(MEAN_CALCULATION_ERROR)

def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    validate_input(sample_values)
    result = calculate_mean(sample_values)
    print(result)