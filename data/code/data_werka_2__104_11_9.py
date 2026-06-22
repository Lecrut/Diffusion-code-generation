from datetime import datetime, timedelta

def calculate_days_difference(start: datetime, end: datetime) -> int:
    delta = end - start
    return delta.days

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 12, 0, 0)
    end_time = datetime(2023, 1, 10, 12, 0, 0)
    result = calculate_days_difference(start_time, end_time)
    print(result)