def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

assert is_leap_year(2000) is True
assert is_leap_year(2024) is True
assert is_leap_year(1900) is False

if __name__ == '__main__':
    test_years = [2000, 2024, 1900, 2023, 2100]
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {result}")