from datetime import datetime
from fractions import Fraction

def fraction_of_month_remaining(year: int, month: int, day: int, hour: int, minute: int, second: int) -> Fraction:
    now = datetime.now()
    if now.year < year or (now.year == year and now.month < month):
        return Fraction(1)
    if now.year > year or (now.year == year and now.month > month):
        return Fraction(0)
    days_in_month_map = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    if is_leap:
        days_in_month_map[2] = 29
    total_days = days_in_month_map[month]
    if month == 12:
        end_date = datetime(year + 1, 1, 1)
    else:
        end_date = datetime(year, month + 1, 1)
    start_of_month = datetime(year, month, 1)
    remaining_time = end_date - now
    total_time_in_month = end_date - start_of_month
    if total_time_in_month.total_seconds() <= 0:
        return Fraction(0)
    if remaining_time.total_seconds() <= 0:
        return Fraction(0)
    fraction = Fraction(remaining_time.total_seconds(), total_time_in_month.total_seconds())
    return fraction
if __name__ == '__main__':
    result = fraction_of_month_remaining(2023, 1, 1, 0, 0, 0)
    print(result)
    result2 = fraction_of_month_remaining(2023, 2, 15, 12, 30, 0)
    print(result2)