import calendar

def is_leap(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    test_years = [2000, 2001, 2004, 1900, 2024, 2100]
    for year in test_years:
        print(f"{year}: {is_leap(year)}")