def is_even(num):
    if not isinstance(num, int) or num < 0:
        raise TypeError("Input must be a non-negative integer.")
    return num % 2 == 0
if __name__ == '__main__':
    test_cases = [42, -5, 1.7]
    for val in test_cases:
        try:
            result = is_even(val)
            print(f"{val} is {'even' if result else 'odd'}")
        except TypeError as e:
            print(e)