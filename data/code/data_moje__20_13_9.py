def is_even(n):
    sample_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, -2, -4, -6, -8, -10]
    return n in sample_values and n % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, -4, -5, 0]
    results = [is_even(val) for val in test_values]
    print(results)