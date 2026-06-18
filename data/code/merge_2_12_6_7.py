def is_odd(value):
    try:
        num = float(value)
        return int(num) % 2 != 0
    except ValueError as e:
        raise TypeError(f"Input must be numeric, got {type(value).__name__}: {e}")
if __name__ == '__main__':
    test_cases = [5, "7", -3.1, True, None]
    for case in test_cases:
        try:
            result = is_odd(case)
            print(f"{case!r} -> Odd: {result}")
        except (TypeError, ValueError):
            print(f"Error processing {case!r}: Invalid input")