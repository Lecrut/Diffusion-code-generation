from datetime import datetime, timedelta
from fractions import Fraction

def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def _days_in_month(year: int, month: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if _is_leap_year(year) else 28
    raise ValueError(f"Invalid month: {month}")

def fraction_of_month_remaining(year: int, month: int, day: int, hour: int, minute: int, second: int) -> Fraction:
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if current_year < year:
        return Fraction(1)
    if current_year > year:
        return Fraction(0)
    if current_month < month:
        return Fraction(1)
    if current_month > month:
        return Fraction(0)

    if current_year == year and current_month == month:
        total_seconds_in_month = _days_in_month(year, month) * 24 * 3600
        elapsed_seconds = (current_day - 1) * 24 * 3600 + current_hour * 3600 + current_minute * 60 + current_second
        remaining_seconds = total_seconds_in_month - elapsed_seconds
        if remaining_seconds < 0:
            return Fraction(0)
        return Fraction(remaining_seconds, total_seconds_in_month)
    
    return Fraction(0)

if __name__ == '__main__':
    result = fraction_of_month_remaining(2023, 1, 1, 0, 0, 0)
    print(result)
    print(float(result))