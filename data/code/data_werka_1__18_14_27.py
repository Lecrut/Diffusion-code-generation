def is_above_threshold(value, threshold):
    return value > threshold

if __name__ == '__main__':
    sample_value = 3.14
    threshold_value = 2.71
    result = is_above_threshold(sample_value, threshold_value)
    print(result)