def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 10, 15, 0, -4, -7]
    for value in test_values:
        print(is_even(value))