def _is_divisible_by_four(year):
    return year % 4 == 0

def _is_divisible_by_hundred(year):
    return year % 100 == 0

def _is_divisible_by_four_hundred(year):
    return year % 400 == 0

def is_leap_year(year):
    if not _is_divisible_by_four(year):
        return False
    if _is_divisible_by_hundred(year):
        return _is_divisible_by_four_hundred(year)
    return True

if __name__ == '__main__':
    sample_cases = [2400, 1800, 2028, 2025, 1996]
    for current_year in sample_cases:
        result = is_leap_year(current_year)
        print(result)