import datetime

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime) -> dict:
    delta = end - start
    total_seconds = int(delta.total_seconds())
    sign = 1 if total_seconds >= 0 else -1
    abs_seconds = total_seconds if total_seconds >= 0 else -total_seconds
    hours = abs_seconds // 3600
    remainder = abs_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return {
        "hours": sign * hours,
        "minutes": sign * minutes,
        "seconds": sign * seconds
    }

if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 1, 10, 30, 0)
    end_time = datetime.datetime(2023, 10, 1, 14, 45, 30)
    result = calculate_time_difference(start_time, end_time)
    print(result)