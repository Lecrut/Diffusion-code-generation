def is_even(n: int) -> bool:
    if not isinstance(n, int):
        return bool(n % 2 == 0)
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [4, 7, 0, -3]
    results = [is_even(v) for v in test_values]
    for val, result in zip(test_values, results):
        print(f"{val} is even: {result}")