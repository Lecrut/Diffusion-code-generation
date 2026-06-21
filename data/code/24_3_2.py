def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2400, 1996, 2100]
    for y in test_years:
        print(is_leap_year(y))