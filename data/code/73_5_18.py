from datetime import datetime

def time_difference(start: datetime, end: datetime) -> timedelta:
    return abs(end - start)

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 12, 0, 0)
    end_time = datetime(2023, 10, 1, 14, 30, 0)
    print(time_difference(start_time, end_time))