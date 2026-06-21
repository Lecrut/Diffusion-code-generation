import calendar

def check_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2000, 2001, 2004, 2023, 2024]
    results = [check_leap_year(y) for y in years]
    print(results)