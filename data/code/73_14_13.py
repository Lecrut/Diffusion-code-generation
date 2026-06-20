from datetime import datetime

def timedelta_to_hours(dt1, dt2):
    delta = dt2 - dt1
    return delta.total_seconds() / 3600.0

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0)
    dt2 = datetime(2023, 4, 1, 15, 30)
    print(timedelta_to_hours(dt1, dt2))