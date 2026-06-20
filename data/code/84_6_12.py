import calendar
DAY_OF_YEAR = 365
LEAP_DAY_OF_YEAR = 366
FEBRUARY = 2

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_number(year: int, month: int, day: int) -> int:
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12')
    if day < 1 or (day > 31 and month not in (4, 6, 9, 11)):
        raise ValueError('Day must be within the valid range for the given month')
    if month == FEBRUARY:
        days_in_month = [0, 29 if is_leap_year(year) else 28]
    else:
        days_in_month = [0, 31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year
if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))