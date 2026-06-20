from datetime import datetime

def timedelta_to_hours(start_dt: datetime, end_dt: datetime) -> float:
    return (end_dt - start_dt).total_seconds() / 3600.0

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 12, 0)
    end = datetime(2023, 10, 1, 14, 30)
    print(timedelta_to_hours(start, end))