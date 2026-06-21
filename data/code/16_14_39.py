def is_positive(value):
    if not isinstance(value, (int, float)):
        return False
    return value > 0

if __name__ == '__main__':
    test_cases = [100, -25, 0.0, 3.14159, -0.0001, 'test', None]
    for case in test_cases:
        print(f"{case}: {is_positive(case)}")