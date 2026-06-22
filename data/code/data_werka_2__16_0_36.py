def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_cases = {
        'positive_integer': 10,
        'negative_integer': -5,
        'zero': 0,
        'positive_float': 3.14,
        'negative_float': -2.7
    }
    
    results = {key: is_positive(value) for key, value in test_cases.items()}
    print(results)