def is_leap_year(year: int) -> bool:
    if year & 3:
        return False
    if year % 100:
        return True
    return not (year % 400)

if __name__ == '__main__':
    test_years = [1600, 1700, 1996, 2000, 2001, 2100, 2400]
    for year in test_years:
        print(is_leap_year(year))