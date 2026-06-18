def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [1, 2, -3, 0]
    results = list(map(is_even, test_cases))
    print(results)