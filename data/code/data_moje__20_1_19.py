def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 15, 100, 101, 42, 255]
    for value in test_values:
        result = is_even(value)
        print(value, result)