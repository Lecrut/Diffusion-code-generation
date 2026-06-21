import calendar

def is_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    test_years = [1900, 2000, 2004, 2023, 2400]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")