import calendar

def is_leap(year: int) -> bool:
    return calendar.isleap(year)

def check_leap_years(years: list) -> dict:
    return {year: is_leap(year) for year in years}

if __name__ == '__main__':
    years = [2000, 2001, 2004, 2023, 2024]
    results = check_leap_years(years)
    for year, is_leap_year in results.items():
        print(f"{year}: {is_leap_year}")