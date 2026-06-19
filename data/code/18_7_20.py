def is_value_above_threshold(value, threshold=10):
    return value > threshold

if __name__ == '__main__':
    test_values = [5, 10, 15, 20]
    for value in test_values:
        result = is_value_above_threshold(value)
        print(f"Value: {value}, Above Threshold: {result}")