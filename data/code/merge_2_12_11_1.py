def is_even(value: int) -> bool:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"Expected integer input, got {type(value).__name__}")
    return value % 2 == 0
if __name__ == '__main__':
    test_cases = [10, -5, 42, True]
    for case in test_cases:
        try:
            result = is_even(case)
            print(f"is_even({case}) -> {result}")
        except TypeError as e:
            print(f"Error checking parity of {case}: {e}")