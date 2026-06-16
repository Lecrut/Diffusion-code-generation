def is_strict_odd_integer(value: int) -> bool:
    return value % 2 != 0
if __name__ == '__main__':
    test_cases = [1, -3, 4, 5.5, "7", True]
    for case in test_cases:
        result = is_strict_odd_integer(case) if isinstance(case, int) else None
        print(f"{case}: {result}")