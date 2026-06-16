def is_odd(n: int) -> bool:
    return n % 2 != 0
if __name__ == '__main__':
    test_cases = [1, -3, 0, 4]
    for val in test_cases:
        print(f"{val}: {is_odd(val)}")