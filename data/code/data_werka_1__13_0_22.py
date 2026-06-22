from datetime import datetime, timedelta

def calculate_time_delta(dt1, dt2):
    return abs(dt1 - dt2)
if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, tzinfo=None)
    dt2 = datetime(2023, 10, 2, 14, 30, tzinfo=None)
    delta = calculate_time_delta(dt1, dt2)
    print(delta)