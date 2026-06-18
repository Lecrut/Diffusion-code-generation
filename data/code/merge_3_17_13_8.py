def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [-1, 0, 3, 4]
    results = [is_even(x) for x in test_cases]
    print(results)