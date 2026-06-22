import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2000, 2021, 2024, 1900]
    results = [is_leap_year(y) for y in years]
    print(results)