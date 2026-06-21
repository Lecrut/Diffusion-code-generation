import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2000, 2023, 2024]
    results = [is_leap_year(y) for y in years]
    for y, res in zip(years, results):
        print(f"{y}: {res}")