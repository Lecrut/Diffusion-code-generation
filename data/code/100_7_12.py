def validate_conditions(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return False
    if a < 0 or b < 0 or c < 0:
        return False
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return True
    if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        (2, 4, 6, False),
        (3, 5, 7, False),
        (2, 3, 5, True),
        (1, 2, 3, False),
        (0, 0, 0, False)
    ]
    for a, b, c, expected in test_cases:
        result = validate_conditions(a, b, c)
        print(f"validate_conditions({a}, {b}, {c}) = {result}, expected: {expected}")