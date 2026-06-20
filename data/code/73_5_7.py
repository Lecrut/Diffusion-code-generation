from datetime import datetime

def time_difference(dt1: datetime, dt2: datetime) -> timedelta:
    return abs(dt1 - dt2)

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 9, 30, 14, 30, 0)
    print(time_difference(sample_dt1, sample_dt2))