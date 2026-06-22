def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = {
        'zero': 0,
        'positive': 1,
        'negative': -1,
        'tiny_positive': 0.0001,
        'tiny_negative': -0.0001,
        'exactly_zero': 0.0
    }
    
    for name, val in test_values.items():
        print(f"{name}: {is_zero(val)}")