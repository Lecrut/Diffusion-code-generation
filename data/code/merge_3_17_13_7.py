def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [1, 2, -3, 4]
    results = [(n, is_even(n)) for n in test_cases]
    print(results)