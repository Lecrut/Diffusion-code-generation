def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5.2, "abc", True]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"is_positive({case}) -> {result}")
        except TypeError as e:
            print(f"Error with input {case}: {e}")