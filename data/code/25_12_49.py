def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [
        (0, True),
        (-0.0, True),
        (1e-308, False),
        (1, False),
        ('0', False),
        (0.001, False)
    ]
    
    for value, expected in test_values:
        result = is_zero(value)
        print(f"is_zero({value}) = {result} (expected: {expected})")