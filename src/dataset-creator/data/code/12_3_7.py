def is_strict_odd_integer(value: int) -> bool:
    return value % 2 != 0
if __name__ == '__main__':
    test_cases = [17, -5, 42, float('inf'), "odd", True]
    for case in test_cases:
        try:
            result = is_strict_odd_integer(case) if isinstance(case, int) else None
            print(f"{case!r}: {result}")
        except TypeError as e:
            print(f"{case!r}: Error - {e}")