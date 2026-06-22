from datetime import datetime, timedelta

DAYS_IN_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
SECONDS_IN_DAY = 86400
START_MONTH = 5
START_YEAR = 2024
SAMPLE_MONTH = 5
SAMPLE_DAY = 15
SAMPLE_HOUR = 14
SAMPLE_MINUTE = 30
SAMPLE_SECOND = 45

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year: int, month: int) -> int:
    days = DAYS_IN_MONTHS[month - 1]
    if month == 2 and is_leap_year(year):
        days = 29
    return days

def compute_remaining_time(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    second: int
) -> timedelta:
    if month < 1 or month > 12:
        raise ValueError(f"Invalid month: {month}")

    current_date = datetime(year, month, day, hour, minute, second)
    
    month_start = datetime(year, month, 1)
    
    days_in_current_month = get_days_in_month(year, month)
    month_end = month_start + timedelta(days=days_in_current_month - 1)
    month_end = month_end.replace(hour=23, minute=59, second=59)
    
    if current_date < month_start:
        return month_end - month_start
    
    if current_date > month_end:
        return timedelta(0)
    
    return month_end - current_date

if __name__ == '__main__':
    result = compute_remaining_time(START_YEAR, START_MONTH, SAMPLE_DAY, SAMPLE_HOUR, SAMPLE_MINUTE, SAMPLE_SECOND)
    print(result)