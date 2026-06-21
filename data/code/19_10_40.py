def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_values = {
        'positive_number': 15,
        'negative_number': -20,
        'zero_value': 0,
        'another_positive': 7,
        'another_negative': -3
    }
    
    results = {}
    for key, value in test_values.items():
        results[key] = is_positive(value)
    
    print(results)