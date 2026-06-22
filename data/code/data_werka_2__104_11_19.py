from datetime import datetime, timedelta

def calculate_days_difference(start: datetime, end: datetime) -> int:
    delta = end - start
    return delta.days

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2023, 1, 10)
    result = calculate_days_difference(dt1, dt2)
    print(result)