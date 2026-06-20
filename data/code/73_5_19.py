from datetime import datetime

def calculate_duration(date1: datetime, date2: datetime) -> int:
    duration = abs(date2 - date1)
    return int(duration.total_seconds())
if __name__ == '__main__':
    date1 = datetime(2023, 4, 1, 12, 0, 0)
    date2 = datetime(2023, 4, 1, 10, 0, 0)
    print(calculate_duration(date1, date2))