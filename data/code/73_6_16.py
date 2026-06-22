from datetime import datetime, timezone, timedelta

def calculate_date_difference(start_date: datetime, end_date: datetime) -> timedelta:
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Both inputs must be datetime objects")
    
    if start_date.tzinfo is None or end_date.tzinfo is None:
        naive_start = start_date.replace(tzinfo=timezone.utc) if start_date.tzinfo is None else start_date
        naive_end = end_date.replace(tzinfo=timezone.utc) if end_date.tzinfo is None else end_date
        diff = naive_end - naive_start
    else:
        diff = end_date - start_date
    
    return diff

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 1, 2, 12, 0, 0, tzinfo=timezone.utc)
    result = calculate_date_difference(dt1, dt2)
    print(result)