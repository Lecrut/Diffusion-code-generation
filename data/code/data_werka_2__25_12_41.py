def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_cases = {
        'integer_zero': 0,
        'negative_zero': -0.0,
        'positive_number': 1,
        'tiny_positive': 0.0001,
        'tiny_negative': -0.0001,
        'exactly_zero_float': 0.0
    }
    for label, number in test_cases.items():
        print(f"{label}: {is_zero(number)}")