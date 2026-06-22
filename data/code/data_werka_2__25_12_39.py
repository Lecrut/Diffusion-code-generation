def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_cases = [
        (0, True),
        (1, False),
        (-0.0, True),
        (0.001, False),
        (1e-308, False),
        ('0', ValueError)
    ]

    for value, expected in test_cases:
        try:
            result = is_zero(value)
            print(f"is_zero({value}) = {result}, expected = {expected}")
        except Exception as e:
            print(f"is_zero({value}) raised {e}, expected {expected}")