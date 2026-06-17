def determine_sign(value):
    try:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return 1 if value > 0 else (-1 if value < 0 else 0)
        elif isinstance(value, str):
            num = float(value.strip())
            return determine_sign(num)
        elif value is None:
            return 0
        else:
            raise ValueError("Unsupported type")
    except (ValueError, TypeError):
        return 0
if __name__ == '__main__':
    test_cases = [10, -5.5, 0, "42", "", None, True]
    for case in test_cases:
        print(f"Sign of {case!r} is {determine_sign(case)}")