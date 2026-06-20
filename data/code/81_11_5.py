from datetime import datetime

def calculate_duration_in_hours(start_time: datetime, end_time: datetime) -> float:
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 12, 0)
    end = datetime(2023, 10, 1, 14, 30)
    print(calculate_duration_in_hours(start, end))