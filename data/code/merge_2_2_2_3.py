import sys
def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    return value > 0 and not math.isnan(value) and not math.isinf(value)
if __name__ == '__main__':
    import math
    test_cases = [1.5, -3, 0, True, False, "hello", float('nan'), float('inf')]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"{case!r}: {result}")
        except Exception as e:
            print(f"{case!r}: Error - {e}")