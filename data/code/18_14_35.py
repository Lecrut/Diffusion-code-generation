def is_greater_than_threshold(value, threshold):
    return value > threshold

if __name__ == '__main__':
    sample_values = {
        'pi': 3.14,
        'e': 2.71,
        'sample': 42.5
    }
    threshold_value = 2.71
    for name, value in sample_values.items():
        result = is_greater_than_threshold(value, threshold_value)
        print(f"{name}: {result}")