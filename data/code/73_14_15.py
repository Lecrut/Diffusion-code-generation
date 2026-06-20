from datetime import datetime

def timedelta_to_hours(dt1: datetime, dt2: datetime) -> float:
    delta = dt2 - dt1
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 4, 1, 12, 0)
    sample_dt2 = datetime(2023, 4, 1, 15, 30)
    print(timedelta_to_hours(sample_dt1, sample_dt2))