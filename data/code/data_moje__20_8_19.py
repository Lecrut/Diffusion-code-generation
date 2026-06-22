def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 2, -2, 100, -100, 13, -13]
    for val in test_values:
        print(is_even(val))