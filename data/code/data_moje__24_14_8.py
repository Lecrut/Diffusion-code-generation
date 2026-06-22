import calendar

def is_leap(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    sample_years = [1900, 1996, 2000, 2023, 2024]
    for year in sample_years:
        result = is_leap(year)
        print(f"{year}: {result}")