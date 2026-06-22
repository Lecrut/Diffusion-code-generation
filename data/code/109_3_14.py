import calendar
from datetime import datetime, timedelta

_MONTH_START_OFFSET = 1
_DAYS_IN_WEEK = 7

def get_days_left_in_current_month(year: int, month: int) -> int:
    total_days = calendar.monthrange(year, month)[1]
    first_day_weekday = calendar.monthrange(year, month)[0]
    days_until_next_month_start = total_days - _MONTH_START_OFFSET + 1
    start_date = datetime(year, month, _MONTH_START_OFFSET)
    next_month_date = start_date + timedelta(days=days_until_next_month_start)
    next_month_date = next_month_date.replace(day=1)
    days_left = (next_month_date - start_date).days
    return days_left

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    days_remaining = get_days_left_in_current_month(sample_year, sample_month)
    print(days_remaining)