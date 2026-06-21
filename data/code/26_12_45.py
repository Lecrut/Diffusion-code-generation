def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be an integer or float')
    if not isinstance(threshold, (int, float)):
        raise TypeError('Threshold must be an integer or float')
    return value > threshold

if __name__ == '__main__':
    test_cases = [
        {'value': 15, 'threshold': 10},
        {'value': 2.8, 'threshold': 3.2},
        {'value': -5, 'threshold': -6},
        {'value': 'abc', 'threshold': 1},
        {'value': 7, 'threshold': 'xyz'}
    ]

    for case in test_cases:
        try:
            result = exceeds_threshold(case['value'], case['threshold'])
            print(f'Value: {case["value"]}, Threshold: {case["threshold"]} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error with Value: {case["value"]}, Threshold: {case["threshold"]} -> {e}')