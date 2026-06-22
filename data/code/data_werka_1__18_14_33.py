def is_greater_than_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float.")
    return value > threshold

if __name__ == '__main__':
    sample_value = 3.14
    threshold_value = 2.71
    result = is_greater_than_threshold(sample_value, threshold_value)
    print(result)