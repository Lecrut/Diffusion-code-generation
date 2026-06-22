import datetime
import calendar
from typing import NamedTuple

DAYS_IN_WEEK = 7
MIN_YEAR = 1
MAX_MONTH = 12
MIN_MONTH = 1
PERCENTAGE_MULTIPLIER = 100.0

class MonthProgress(NamedTuple):
    total_days: int
    days_passed: int
    days_remaining: int
    percentage_completed: float

def calculate_month_progress(year: int, month: int) -> MonthProgress:
    if not (MIN_MONTH <= month <= MAX_MONTH):
        raise ValueError(f"Month must be between {MIN_MONTH} and {MAX_MONTH}")
    if year < MIN_YEAR:
        raise ValueError(f"Year must be at least {MIN_YEAR}")
    
    today = datetime.date.today()
    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = datetime.date(year, month, calendar.monthrange(year, month)[1])
    
    total_days = last_day_of_month.day
    days_passed = 0
    days_remaining = total_days
    
    if today < first_day_of_month:
        days_passed = 0
        days_remaining = total_days
    elif today > last_day_of_month:
        days_passed = total_days
        days_remaining = 0
    else:
        delta = today - first_day_of_month
        days_passed = delta.days + 1
        days_remaining = total_days - days_passed
    
    percentage_completed = (days_passed / total_days) * PERCENTAGE_MULTIPLIER
    
    return MonthProgress(
        total_days=total_days,
        days_passed=days_passed,
        days_remaining=days_remaining,
        percentage_completed=percentage_completed
    )

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    result = calculate_month_progress(sample_year, sample_month)
    print(result)