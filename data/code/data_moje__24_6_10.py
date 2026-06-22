def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2100, 1600]
    for y in test_years:
        print(y, is_leap_year(y))