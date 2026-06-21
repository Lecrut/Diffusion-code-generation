import calendar

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2024, 1900, 2000, 2023]
    for year in years:
        print(year, is_leap_year(year))