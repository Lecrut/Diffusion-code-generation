from datetime import datetime

def elapsed_time_in_hours(start_dt, end_dt):
    delta = end_dt - start_dt
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 12, 0, 0)
    end = datetime(2023, 10, 1, 14, 30, 0)
    print(elapsed_time_in_hours(start, end))