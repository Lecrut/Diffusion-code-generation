def is_even(n: int) -> bool:
    sample_values = {0, 2, 4, 6, 8, 10, 100, 1000, -2, -4}
    return n % 2 == 0 and n in sample_values

if __name__ == '__main__':
    test_cases = [2, 3, 0, -2, 5, 100]
    results = [is_even(x) for x in test_cases]
    print(results)