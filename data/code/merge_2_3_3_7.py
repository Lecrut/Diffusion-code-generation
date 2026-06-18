def is_even(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -3, "5", 1.7]
    for case in test_cases:
        try:
            result = is_even(case)
            print(f"{case} is {'even' if result else 'odd'}")
        except TypeError as e:
            print(f"Error processing {case}: {e}")