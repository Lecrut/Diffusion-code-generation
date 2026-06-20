def check_complex_condition(a, b, c, d):
    MIN_A = 10
    MAX_B = 20
    THRESHOLD_C = 50
    MULTIPLIER_D = 3
    if a < MIN_A:
        return False
    if b > MAX_B:
        return False
    if c <= THRESHOLD_C:
        return True
    if d * MULTIPLIER_D >= THRESHOLD_C:
        return True
    return False
if __name__ == '__main__':
    test_cases = [(15, 18, 45, 2), (9, 25, 60, 3), (10, 15, 50, 1), (11, 19, 49, 2)]
    for a, b, c, d in test_cases:
        result = check_complex_condition(a, b, c, d)
        print(f'check_complex_condition({a}, {b}, {c}, {d}) = {result}')