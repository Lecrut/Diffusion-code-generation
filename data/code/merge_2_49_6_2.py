from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0 and isinstance(value, (int, float))
if __name__ == '__main__':
    test_cases = [5, -3.5, 0, '1', None]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"{case}: {result}")
        except TypeError:
            print(f"{case}: Not a number")