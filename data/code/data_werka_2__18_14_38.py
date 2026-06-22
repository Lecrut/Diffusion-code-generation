def validate_float(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an int or float")

def is_greater_than_threshold(value, threshold):
    validate_float(value)
    validate_float(threshold)
    return value > threshold

if __name__ == '__main__':
    sample_value = 7.0
    threshold_value = 5.5
    result = is_greater_than_threshold(sample_value, threshold_value)
    print(result)