def is_leap_year(year):
    if not isinstance(year, int) or year <= 0:
        return False
    div_by_4 = (year & 3) == 0
    div_by_100 = (year % 100) == 0
    div_by_400 = (year % 400) == 0
    if div_by_100:
        return div_by_400
    return div_by_4

assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2024) == True
assert is_leap_year(2023) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 1800, 2400, 2100, 2004, 2001]
    for y in test_years:
        print(is_leap_year(y))