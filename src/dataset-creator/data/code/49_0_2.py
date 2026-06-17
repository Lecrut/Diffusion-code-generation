import sys
def check_positive(value: int | float) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(value).__name__}")
    return value > 0
if __name__ == '__main__':
    test_cases = [42, -5.7, 0, 3.14]
    for case in test_cases:
        try:
            result = check_positive(case)
            print(f"{case} is positive: {result}")
        except TypeError as e:
            print(f"Error checking {case}: {e}", file=sys.stderr)