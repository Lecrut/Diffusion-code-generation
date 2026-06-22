ZERO_THRESHOLD = 1e-10

def is_zero(value):
    return abs(value) < ZERO_THRESHOLD

if __name__ == '__main__':
    test_values = {
        'zero': 0,
        'positive_small': 1e-9,
        'negative_small': -1e-9,
        'tiny_positive': 1e-15,
        'tiny_negative': -1e-15,
        'exactly_zero': 0.0
    }
    for name, val in test_values.items():
        print(f"{name}: {is_zero(val)}")