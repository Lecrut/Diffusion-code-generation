def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, -2, 1, -5, 100, -100]
    for value in test_values:
        result = is_even(value)
        print(f"Value: {value}, Is Even: {result}")