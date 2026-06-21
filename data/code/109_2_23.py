from datetime import datetime, timedelta

SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12

HARD_CODED_START = datetime(2024, 5, 1)
HARD_CODED_END = datetime(2024, 5, 31, 23, 59, 59)
HARD_CODED_NOW = datetime(2024, 5, 15, 10, 30, 0)

def calculate_remaining_time(start: datetime, end: datetime, current: datetime) -> timedelta:
    if current < start:
        return end - start
    if current >= end:
        return timedelta(0)
    return end - current

def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    days = total_seconds // SECONDS_IN_DAY
    remaining_seconds = total_seconds % SECONDS_IN_DAY
    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds = remaining_seconds % SECONDS_IN_HOUR
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    seconds = remaining_seconds % SECONDS_IN_MINUTE
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    result = calculate_remaining_time(HARD_CODED_START, HARD_CODED_END, HARD_CODED_NOW)
    print(format_timedelta(result))