def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_cases = {
        'positive_number': 15,
        'negative_number': -8,
        'zero': 0,
        'another_positive': 27,
        'another_negative': -3
    }
    results = {key: is_positive(value) for key, value in test_cases.items()}
    print(results)