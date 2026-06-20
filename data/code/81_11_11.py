from datetime import datetime

def calculate_duration_in_hours(start: datetime, end: datetime) -> float:
    return (end - start).total_seconds() / 3600

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 12, 0)
    end_time = datetime(2023, 10, 1, 14, 30)
    print(calculate_duration_in_hours(start_time, end_time))