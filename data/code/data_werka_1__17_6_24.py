def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    results = {n: is_even(n) for n in test_cases}
    print(results)