def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or a floating-point number.")
    return value > 0
if __name__ == '__main__':
    test_cases = [42.5, -17, 0, 3e-8, None]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"is_positive({case}) -> {result}")
        except TypeError as e:
            print(f"Error checking {case}: {e}")