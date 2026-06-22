def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be an integer or float')
    if not isinstance(threshold, (int, float)):
        raise TypeError('Threshold must be an integer or float')
    return value > threshold
if __name__ == '__main__':
    sample_value = 10
    sample_threshold = 5
    result = exceeds_threshold(sample_value, sample_threshold)
    print(result)
    sample_value2 = 3.5
    sample_threshold2 = 4.0
    result2 = exceeds_threshold(sample_value2, sample_threshold2)
    print(result2)
    try:
        invalid_value = '10'
        result3 = exceeds_threshold(invalid_value, sample_threshold)
    except TypeError as e:
        print(e)