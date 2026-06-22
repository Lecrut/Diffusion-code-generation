def is_even(n: int) -> bool:
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 100, 101, -5, 10**18]
    results = [is_even(n) for n in test_values]
    for n, res in zip(test_values, results):
        print(f"is_even({n}) = {res}")