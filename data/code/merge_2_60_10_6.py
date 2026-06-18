import calendar
def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)
if __name__ == '__main__':
    sample_years = [1900, 2000, 2024]
    for test_year in sample_years:
        result = is_leap_year(test_year)
        print(f"{test_year} is a {'leap' if result else 'non-leap'} year.")