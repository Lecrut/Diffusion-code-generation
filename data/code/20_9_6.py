def _validate_int(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

def is_even(n):
    _validate_int(n)
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 13, -4, -5, 100, 99]
    for val in test_values:
        print(is_even(val))