import datetime

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime) -> dict:
    delta = end - start
    total_seconds = int(delta.total_seconds())
    sign = 1 if total_seconds >= 0 else -1
    abs_seconds = total_seconds * sign
    hours = abs_seconds // SECONDS_PER_HOUR
    remainder_after_hours = abs_seconds % SECONDS_PER_HOUR
    minutes = remainder_after_hours // SECONDS_PER_MINUTE
    seconds = remainder_after_hours % SECONDS_PER_MINUTE
    return {
        "hours": sign * hours,
        "minutes": sign * minutes,
        "seconds": sign * seconds
    }

if __name__ == '__main__':
    start_time = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime.datetime(2023, 1, 1, 12, 30, 45)
    result = calculate_time_difference(start_time, end_time)
    print(result)