import calendar
def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y} is a leap year" if result else f"{y} is not a leap year")