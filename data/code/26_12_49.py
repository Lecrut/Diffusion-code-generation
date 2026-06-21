def exceeds_threshold(value, threshold):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be an integer or float')
    if not isinstance(threshold, (int, float)):
        raise TypeError('Threshold must be an integer or float')
    return value > threshold

if __name__ == '__main__':
    test_cases = {
        'case1': {'value': 10, 'threshold': 5},
        'case2': {'value': 3.5, 'threshold': 4.0},
        'case3': {'value': -2, 'threshold': -3},
        'case4': {'value': 'a', 'threshold': 1},
        'case5': {'value': 7, 'threshold': 'b'},
    }

    for case_name, params in test_cases.items():
        try:
            result = exceeds_threshold(params['value'], params['threshold'])
            print(f'{case_name}: Value: {params["value"]}, Threshold: {params["threshold"]} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error in {case_name} with Value: {params["value"]}, Threshold: {params["threshold"]} -> {e}')