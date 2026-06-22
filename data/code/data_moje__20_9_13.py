def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [18, 25, 0, -12, 1001]
    for value in test_values:
        print(f"{value}: {is_even(value)}")