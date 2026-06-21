def is_even(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 42, -1, -100, 999]
    for value in test_values:
        print(is_even(value))