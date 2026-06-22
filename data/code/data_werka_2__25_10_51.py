def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'positive_integer': 5,
        'negative_integer': -3,
        'floating_point': 0.0,
        'non_numeric_string': 'hello',
        'empty_string': '',
        'none_value': None
    }
    
    results = {key: is_zero(value) for key, value in test_cases.items()}
    print(results)