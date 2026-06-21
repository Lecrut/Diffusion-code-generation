import calendar
from datetime import datetime, date

def days_left_in_current_month(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    last_day = calendar.monthrange(year, month)[1]
    if day > last_day:
        raise ValueError(f"Day {day} is not valid for month {month} of year {year}")
    current_date = date(year, month, day)
    next_month_first = date(year, month + 1, 1) if month < 12 else date(year + 1, 1, 1)
    days_left = (next_month_first - current_date).days
    return days_left

if __name__ == '__main__':
    result = days_left_in_current_month(2023, 10, 15)
    print(result)