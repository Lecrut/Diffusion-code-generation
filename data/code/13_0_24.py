from datetime import datetime, timedelta

def calculate_time_delta(dt1, dt2):
    return abs(dt2 - dt1)
if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, tzinfo='UTC')
    dt2 = datetime(2023, 10, 2, 15, 30, tzinfo='UTC')
    delta = calculate_time_delta(dt1, dt2)
    print(delta)