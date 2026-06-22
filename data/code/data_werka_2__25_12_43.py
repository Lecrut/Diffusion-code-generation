def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_cases = [0, 1, -0.0, 0.001, 1e-308, '0', None]
    for case in test_cases:
        print(f"is_zero({case}): {is_zero(case)}")