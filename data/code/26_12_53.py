def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be an integer or float')
    if not isinstance(threshold, (int, float)):
        raise TypeError('Threshold must be an integer or float')
    return value > threshold

if __name__ == '__main__':
    sample_values = {
        'test1': {'value': 10, 'threshold': 5},
        'test2': {'value': 3.5, 'threshold': 4.0},
        'test3': {'value': -2, 'threshold': -3},
        'test4': {'value': 'a', 'threshold': 1},
        'test5': {'value': 7, 'threshold': 'b'}
    }
    
    for test_name, data in sample_values.items():
        try:
            result = exceeds_threshold(data['value'], data['threshold'])
            print(f'Test {test_name}: Value: {data["value"]}, Threshold: {data["threshold"]} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error in Test {test_name} with Value: {data["value"]}, Threshold: {data["threshold"]} -> {e}')