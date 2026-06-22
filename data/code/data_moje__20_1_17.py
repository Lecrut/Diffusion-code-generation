def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    test_cases = [12, 13, -8, -7, 0]
    for case in test_cases:
        try:
            print(is_even(case))
        except TypeError as e:
            print(f"Error: {e}")