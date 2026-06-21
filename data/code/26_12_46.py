def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be an integer or float')
    if not isinstance(threshold, (int, float)):
        raise ValueError('Threshold must be an integer or float')
    return value > threshold

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3.5, 4.0),
        (-2, -3),
        ('a', 1),
        (7, 'b'),
        (8, 8)
    ]
    
    for value, threshold in test_cases:
        try:
            result = exceeds_threshold(value, threshold)
            print(f'Value: {value}, Threshold: {threshold} -> Exceeds: {result}')
        except ValueError as e:
            print(f'Error with Value: {value}, Threshold: {threshold} -> {e}')