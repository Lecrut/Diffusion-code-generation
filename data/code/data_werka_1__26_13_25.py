def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Threshold must be an integer or float")
    return value > threshold

if __name__ == '__main__':
    sample_value = 10
    sample_threshold = 5
    result = exceeds_threshold(sample_value, sample_threshold)
    print(result)