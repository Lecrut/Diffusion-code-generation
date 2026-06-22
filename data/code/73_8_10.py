from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    return end - start

if __name__ == '__main__':
    start_dt = datetime(2023, 1, 1, 10, 0, 0)
    end_dt = datetime(2023, 1, 1, 12, 30, 45)
    result = calculate_time_difference(start_dt, end_dt)
    print(result)