def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    return value > 0
if __name__ == '__main__':
    test_cases = [10, -5.5, 3.99, 0, "invalid", True]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"{case}: {result}")
        except TypeError as e:
            print(f"Error with input '{case}': {e}")