from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    return end - start

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime(2023, 1, 1, 10, 0, 0)
    result = calculate_time_difference(dt1, dt2)
    print(result)