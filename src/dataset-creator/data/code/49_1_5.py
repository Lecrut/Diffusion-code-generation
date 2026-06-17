def determine_sign(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return 1 if value > 0 else (-1 if value < 0 else 0)
    return None
if __name__ == '__main__':
    test_cases = [5.2, -3, 0, "invalid", None]
    for case in test_cases:
        print(f"Sign of {case}: {determine_sign(case)}")