def is_greater_than_threshold(number, threshold):
    return number > threshold

if __name__ == '__main__':
    sample_number = 42.5
    sample_threshold = 30.0
    result = is_greater_than_threshold(sample_number, sample_threshold)
    print(result)