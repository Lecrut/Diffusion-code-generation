from datetime import datetime, timedelta

def calculate_time_delta(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError('Both datetime objects must be timezone-aware.')
    time_difference = abs(dt1 - dt2)
    return time_difference
if __name__ == '__main__':
    dt1 = datetime(2023, 9, 15, 8, 45, tzinfo=datetime.timezone(datetime.timedelta(hours=-6)))
    dt2 = datetime(2023, 9, 17, 13, 15, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    delta = calculate_time_delta(dt1, dt2)
    print(delta)