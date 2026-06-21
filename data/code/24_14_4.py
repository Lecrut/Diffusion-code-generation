import calendar

def check_leap_years(years):
    return {year: calendar.isleap(year) for year in years}

if __name__ == '__main__':
    sample_years = [2000, 2001, 2004, 1900, 2024]
    results = check_leap_years(sample_years)
    for year, is_leap in results.items():
        print(f"{year}: {'Yes' if is_leap else 'No'}")