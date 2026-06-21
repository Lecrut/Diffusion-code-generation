def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'positive_integer': 1,
        'negative_integer': -1,
        'positive_float': 0.001,
        'negative_float': -0.001,
        'exactly_zero_float': 0.0,
        'negative_zero': -0.0,
        'extremely_small_positive': 1e-308
    }
    
    for description, value in test_cases.items():
        print(f"{description}: {is_zero(value)}")