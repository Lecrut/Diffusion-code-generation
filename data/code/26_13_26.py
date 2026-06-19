def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Threshold must be an integer or float")
    return value > threshold

if __name__ == '__main__':
    sample_values = [
        {'value': 10, 'threshold': 5},
        {'value': 3.5, 'threshold': 4.2},
        {'value': -2, 'threshold': -3},
        {'value': 0, 'threshold': 0}
    ]

    for sample in sample_values:
        result = exceeds_threshold(sample['value'], sample['threshold'])
        print(f"Value: {sample['value']}, Threshold: {sample['threshold']} -> Exceeds: {result}")