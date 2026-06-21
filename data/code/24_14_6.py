import calendar

def is_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    years = [2020, 2021, 2000, 1900, 2400]
    for y in years:
        print(f"{y}: {is_leap_year(y)}")