def is_leap_year(year: int) -> bool:
    if year < 1:
        return False
    mod_4 = year & 3 == 0
    if not mod_4:
        return False
    mod_100 = year % 100 == 0
    if mod_100:
        mod_400 = year % 400 == 0
        return mod_400
    return True

def verify_leap_year(year: int, expected: bool) -> bool:
    result = is_leap_year(year)
    if result != expected:
        raise AssertionError(f'Leap year check failed for {year}: expected {expected}, got {result}')
    return result
if __name__ == '__main__':
    test_cases = [(2000, True), (1900, False), (2004, True), (2003, False), (1600, True), (1700, False), (1800, False), (2100, False), (4, True), (1, False), (0, False), (-4, False)]
    all_passed = True
    results = []
    for year, expected in test_cases:
        passed = verify_leap_year(year, expected)
        result_val = is_leap_year(year)
        results.append(result_val)
        if not passed:
            all_passed = False
    print(results)