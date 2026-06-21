import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    years_to_check = [2000, 1900, 2024, 2023, 2100]
    for year in years_to_check:
        result = is_leap_year(year)
        print(f"{year}: {result}")