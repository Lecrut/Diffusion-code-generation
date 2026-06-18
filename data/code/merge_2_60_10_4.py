import calendar
def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)
if __name__ == '__main__':
    sample_years = [1900, 2000, 2024]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year}: {'Leap' if result else 'Not Leap'}")