from datetime import datetime

def timedelta_to_hours(dt1, dt2):
    delta = abs(dt2 - dt1)
    hours = delta.total_seconds() / 3600.0
    return hours

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 2, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 2, 1, 14, 30, 0)
    result = timedelta_to_hours(sample_dt1, sample_dt2)
    print(result)