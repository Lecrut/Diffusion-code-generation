from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    delta = end - start
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        return -delta
    return delta

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 12, 0, 0)
    end_time = datetime(2023, 1, 1, 10, 0, 0)
    result = calculate_time_difference(start_time, end_time)
    print(result)