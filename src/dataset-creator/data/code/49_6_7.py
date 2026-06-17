from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0 and isinstance(value, (int, float))
if __name__ == '__main__':
    test_cases = [1, -5, 3.14, 0, "a", None]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"{case!r}: {result}")
        except TypeError as e:
            print(f"{case!r}: Error - {e}")