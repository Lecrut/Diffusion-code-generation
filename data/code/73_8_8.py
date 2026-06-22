from datetime import datetime, timedelta

UNITS_TO_SECONDS = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800,
}

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError("Both arguments must be datetime objects")
    return end - start

if __name__ == '__main__':
    start_time = datetime(2024, 1, 1, 0, 0, 0)
    end_time = datetime(2024, 1, 2, 12, 30, 0)
    diff = calculate_time_difference(start_time, end_time)
    print(diff)