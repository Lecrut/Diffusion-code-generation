def get_sign(value):
    if value is None:
        return 0
    try:
        num = float(value)
        if num == 0:
            return 0
        elif num > 0:
            return 1
        else:
            return -1
    except (ValueError, TypeError):
        return None
if __name__ == '__main__':
    test_cases = [5, -3.5, "invalid", "", None]
    for case in test_cases:
        result = get_sign(case)
        print(f"Input: {case!r} -> Sign: {result}")