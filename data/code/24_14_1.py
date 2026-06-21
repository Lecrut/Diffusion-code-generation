import calendar

def is_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2100, 2400]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y}: {result}")