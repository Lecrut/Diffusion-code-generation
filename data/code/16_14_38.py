def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    test_cases = [100, -25, 0.0, 3.14159, -1e-6, 'world', None]
    for case in test_cases:
        result = is_positive(case)
        print(f"{case}: {result}")