from datetime import datetime

def duration_in_hours(start_time, end_time):
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 12, 0)
    end = datetime(2023, 10, 1, 14, 30)
    print(duration_in_hours(start, end))