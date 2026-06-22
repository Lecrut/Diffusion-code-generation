def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'positive_int': 5,
        'negative_int': -3,
        'float_zero': 0.0,
        'non_numeric': None,
        'string_zero': '0',
        'empty_list': [],
        'empty_dict': {}
    }
    results = {key: is_zero(value) for key, value in test_cases.items()}
    print(results)