def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 100, 999, -2, -1]
    results = [is_even(val) for val in test_values]
    print(results)