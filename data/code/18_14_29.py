def is_greater_than_threshold(value, threshold):
    return value > threshold

if __name__ == '__main__':
    sample_value = 10.5
    threshold_value = 5.0
    result = is_greater_than_threshold(sample_value, threshold_value)
    print(result)