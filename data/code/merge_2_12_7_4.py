def is_odd(n: int) -> bool:
    return n % 2 != 0
if __name__ == '__main__':
    test_cases = [-3, -2, 0, 1, 5, 10]
    for val in test_cases:
        print(f"{val}: {is_odd(val)}")