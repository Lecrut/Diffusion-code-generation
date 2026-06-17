import calendar
def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year} is {'a' if result else 'not a'} leap year.")