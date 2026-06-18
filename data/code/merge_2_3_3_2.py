def is_even(number):
    if not isinstance(number, int) or number < 0:
        raise TypeError("Input must be a non-negative integer.")
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -5, "10", 3.5]
    for case in test_cases:
        try:
            result = is_even(case)
            print(f"{case} -> {result}")
        except TypeError as e:
            print(f"Error processing {case}: {e}")