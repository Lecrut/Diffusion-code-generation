from datetime import datetime

def elapsed_time_in_hours(start: datetime, end: datetime) -> float:
    delta = end - start
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 12, 0, 0)
    end_time = datetime(2023, 10, 1, 14, 30, 0)
    print(elapsed_time_in_hours(start_time, end_time))