def is_greater_than_threshold(value, threshold):
    if not isinstance(value, float):
        raise ValueError("The value must be a float.")
    return value > threshold

if __name__ == '__main__':
    sample_value = 3.14
    threshold_value = 2.71
    result = is_greater_than_threshold(sample_value, threshold_value)
    print(result)