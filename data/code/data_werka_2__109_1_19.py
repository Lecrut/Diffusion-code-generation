from datetime import datetime, timedelta

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

def seconds_left_in_month(timestamp: float) -> int:
    dt = datetime.fromtimestamp(timestamp)
    if dt.month == 12:
        next_month = datetime(dt.year + 1, 1, 1)
    else:
        next_month = datetime(dt.year, dt.month + 1, 1)
    first_of_next_month = next_month.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = first_of_next_month - dt
    total_seconds = delta.days * SECONDS_IN_DAY + delta.seconds
    return int(total_seconds)

if __name__ == '__main__':
    sample_timestamp = 1672531200
    result = seconds_left_in_month(sample_timestamp)
    print(result)