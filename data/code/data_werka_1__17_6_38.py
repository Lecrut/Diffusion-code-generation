def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [0, 1, -1, 2, -2, 3, -3, 100, -100]
    results = {case: is_even(case) for case in test_cases}
    print(results)