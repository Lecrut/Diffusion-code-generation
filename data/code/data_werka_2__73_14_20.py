import datetime

def calculate_time_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> dict:
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds = abs(total_seconds)
        sign = -1
    else:
        sign = 1
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return {
        "hours": sign * hours,
        "minutes": sign * minutes,
        "seconds": sign * seconds
    }

if __name__ == '__main__':
    start = datetime.datetime(2023, 10, 1, 10, 30, 0)
    end = datetime.datetime(2023, 10, 1, 12, 45, 30)
    result = calculate_time_difference(start, end)
    print(result)