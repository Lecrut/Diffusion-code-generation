def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -3, 0, 1, 2, 3, 4]
    results = []
    for val in test_values:
        results.append(is_even(val))
    print(results)