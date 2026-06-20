from datetime import datetime

def compare_datetimes_ignoring_time(dt1: datetime, dt2: datetime) -> bool:
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise ValueError("Both arguments must be instances of datetime.datetime")
    
    return dt1.date() == dt2.date()

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 15, 12, 30)
    dt2 = datetime(2023, 4, 15, 18, 45)
    print(compare_datetimes_ignoring_time(dt1, dt2))