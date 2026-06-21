def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, -1, -2, 4, -4, 7, -7]
    for value in test_values:
        print(value, is_even(value))