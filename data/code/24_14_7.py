import calendar

def is_leap_year(year):
    return calendar.isleap(year)

if __name__ == '__main__':
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(1900))
    print(is_leap_year(2000))
    print(is_leap_year(2025))