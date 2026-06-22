def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [4, 7, -2, 0, 100, 101]
    for value in test_values:
        print(is_even(value))