from datetime import datetime, timedelta

def calculate_days_difference(dt1: datetime, dt2: datetime) -> int:
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise ValueError("Both inputs must be datetime objects")
    delta = dt1 - dt2
    return delta.days

if __name__ == '__main__':
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    result = calculate_days_difference(start_date, end_date)
    print(result)