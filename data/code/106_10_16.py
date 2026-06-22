from datetime import datetime

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_february(year: int) -> int:
    return 29 if is_leap_year(year) else 28

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError('Inputs must be datetime objects')
    if date1 == date2:
        return 0
    earlier = date1 if date1 < date2 else date2
    later = date2 if date1 < date2 else date1
    year_diff = later.year - earlier.year
    if year_diff == 0:
        return 0
    earlier_month = earlier.month
    earlier_day = earlier.day
    if earlier_month == 2 and earlier_day == 29:
        earlier_month = 2
        earlier_day = 28
    try:
        anniversary = datetime(later.year, earlier_month, earlier_day)
    except ValueError:
        anniversary = datetime(later.year, 2, 28)
    if later < anniversary:
        year_diff -= 1
    return year_diff
if __name__ == '__main__':
    d1 = datetime(2000, 2, 29)
    d2 = datetime(2024, 2, 28)
    result = calculate_year_difference(d1, d2)
    print(result)