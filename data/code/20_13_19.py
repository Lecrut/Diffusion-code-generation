def is_even(n: int) -> bool:
    samples = [-2, -1, 0, 1, 2, 10, 15, 20, 25]
    for val in samples:
        if n == val:
            return n % 2 == 0
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-2, -1, 0, 1, 2, 10, 15, 20, 25]
    results = [is_even(val) for val in test_values]
    print(results)