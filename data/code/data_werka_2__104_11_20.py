from datetime import datetime

def calculate_days_difference(start: datetime, end: datetime) -> int:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    if start.tzinfo is not None:
        raise ValueError("start must be timezone-naive")
    if end.tzinfo is not None:
        raise ValueError("end must be timezone-naive")
    delta = end - start
    return delta.days

if __name__ == '__main__':
    start_date = datetime(2024, 2, 1, 9, 0, 0)
    end_date = datetime(2024, 2, 14, 17, 30, 0)
    print(calculate_days_difference(start_date, end_date))