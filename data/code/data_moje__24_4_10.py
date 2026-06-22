def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

assert is_leap_year(2000) is True
assert is_leap_year(1900) is False
assert is_leap_year(2024) is True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    for y in test_years:
        print(is_leap_year(y))