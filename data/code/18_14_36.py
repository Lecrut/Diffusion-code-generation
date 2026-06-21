def is_greater_than_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise ValueError("The value must be an integer or float.")
    if not isinstance(threshold, (int, float)):
        raise ValueError("The threshold must be an integer or float.")
    return value > threshold

if __name__ == '__main__':
    try:
        sample_value = 5.67
        threshold_value = 4.23
        result = is_greater_than_threshold(sample_value, threshold_value)
        print(result)
    except ValueError as e:
        print(e)