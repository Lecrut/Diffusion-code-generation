from datetime import datetime

HOURS_PER_DAY = 24.0
MINUTES_PER_HOUR = 60.0
SECONDS_PER_MINUTE = 60.0
SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE

def get_hours_between(start_dt: datetime, end_dt: datetime) -> float:
    difference = end_dt - start_dt
    total_seconds = difference.total_seconds()
    return total_seconds / SECONDS_PER_HOUR

if __name__ == '__main__':
    time_start = datetime(2025, 12, 1, 6, 15, 0)
    time_end = datetime(2025, 12, 1, 10, 45, 0)
    diff_hours = get_hours_between(time_start, time_end)
    print(diff_hours)