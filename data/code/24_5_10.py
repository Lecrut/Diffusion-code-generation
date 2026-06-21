def check_leap(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == '__main__':
    test_years = [2024, 1900, 2000, 2023, 2400, 1800, 2100, 2028]
    for year in test_years:
        print(check_leap(year))