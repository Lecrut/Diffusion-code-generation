def check_parity(value):
    if isinstance(value, (int, float)):
        return value > 0 and int(value) % 2 != 0
    raise TypeError("Input must be an integer or float")
if __name__ == '__main__':
    test_cases = [1.5, -3, 4, 7, 8.9]
    for case in test_cases:
        print(f"{case}: {check_parity(case)}")