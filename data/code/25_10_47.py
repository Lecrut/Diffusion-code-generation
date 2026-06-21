def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'positive_int': 1,
        'negative_int': -1,
        'float_number': 2.5,
        'none_value': None,
        'string_zero': '0',
        'empty_list': [],
        'empty_dict': {}
    }
    
    results = {key: is_zero(value) for key, value in test_cases.items()}
    print(results)