def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or float")
    return value > 0
if __name__ == '__main__':
    test_cases = [10.5, -3, 0, 42]
    for case in test_cases:
        result = is_positive(case)
        print(f"{case}: {result}")