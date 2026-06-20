from datetime import datetime, timezone

def time_delta_in_hours(dt1, dt2):
    return (dt1.astimezone(timezone.utc) - dt2.astimezone(timezone.utc)).total_seconds() / 3600

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 10, 0, 0, tzinfo=timezone.utc)
    print(time_delta_in_hours(dt1, dt2))