def _is_divisible_by(numerator, denominator):
    return numerator % denominator == 0

def _check_century_rule(year):
    if _is_divisible_by(year, 100):
        return _is_divisible_by(year, 400)
    return True

def is_leap_year(year):
    if not _is_divisible_by(year, 4):
        return False
    return _check_century_rule(year)

if __name__ == '__main__':
    samples = [2000, 1900, 2024, 2023, 1600, 1700, 2400, 2100, 2025, 2028]
    for y in samples:
        result = is_leap_year(y)
        print(f"{y}: {result}")