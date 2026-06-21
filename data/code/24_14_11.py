import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    for year in test_years:
        print(year, is_leap_year(year))