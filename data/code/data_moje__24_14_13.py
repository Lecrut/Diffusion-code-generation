import calendar

def is_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2000, 1900, 2024, 2023, 2004]
    for year in years:
        print(f"{year}: {is_leap_year(year)}")