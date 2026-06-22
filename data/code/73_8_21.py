import datetime

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime) -> datetime.timedelta:
    if not isinstance(start, datetime.datetime) or not isinstance(end, datetime.datetime):
        raise ValueError("Both arguments must be datetime objects")
    return end - start

if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 1, 10, 0, 0)
    end_time = datetime.datetime(2023, 10, 1, 12, 30, 45)
    result = calculate_time_difference(start_time, end_time)
    print(result)