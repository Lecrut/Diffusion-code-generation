def check_parity(value):
    if isinstance(value, (int, float)):
        is_integer = value.is_integer() if isinstance(value, float) else True
        return is_integer and value > 0 and value % 2 != 0
    return False
if __name__ == '__main__':
    test_cases = [1.5, -3, 4, 7, 8.0, 9]
    for case in test_cases:
        print(f"{case}: {check_parity(case)}")