import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2000, 1900, 2023, 2024, 2100]
    results = [(y, is_leap_year(y)) for y in years]
    for y, result in results:
        print(result)