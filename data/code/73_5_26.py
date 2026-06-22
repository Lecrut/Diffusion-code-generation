from datetime import datetime, timedelta

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
SECONDS_PER_SECOND = 1

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    delta = end - start
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        return timedelta(seconds=-total_seconds)
    return delta

if __name__ == '__main__':
    start_time = datetime(2023, 11, 15, 14, 30, 0)
    end_time = datetime(2023, 11, 15, 12, 15, 0)
    result = calculate_time_difference(start_time, end_time)
    print(result)