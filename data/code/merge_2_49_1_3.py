def get_sign(value):
    try:
        if value is None:
            return 0
        num = float(value)
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    except (ValueError, TypeError):
        return 0
if __name__ == '__main__':
    test_cases = [5, -3.5, 0, "hello", None, True]
    for case in test_cases:
        print(f"Input: {case!r} -> Sign: {get_sign(case)}")