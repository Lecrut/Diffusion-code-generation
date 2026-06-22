from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    delta = end - start
    total_seconds = delta.total_seconds()
    return delta if total_seconds >= 0 else -delta

if __name__ == '__main__':
    start_time = datetime(2024, 5, 15, 14, 30, 0)
    end_time = datetime(2024, 5, 15, 10, 15, 0)
    result = calculate_time_difference(start_time, end_time)
    print(result)