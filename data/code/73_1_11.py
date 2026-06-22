from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
HOURS_IN_DAY = 24
SECONDS_IN_DAY = HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
MICROSECONDS_IN_SECOND = 1_000_000

def calculate_time_diff(date_string1: str, date_string2: str) -> timedelta:
    parser = lambda s: datetime.fromisoformat(s)
    dt_first = parser(date_string1)
    dt_second = parser(date_string2)
    return dt_second - dt_first

if __name__ == '__main__':
    start_str = "2024-02-28T09:00:00"
    end_str = "2024-03-01T14:30:00"
    delta = calculate_time_diff(start_str, end_str)
    print(delta)