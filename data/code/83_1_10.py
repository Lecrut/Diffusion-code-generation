import datetime

def compare_datetimes_ignoring_time(dt1: datetime.datetime, dt2: datetime.datetime) -> bool:
    if not isinstance(dt1, datetime.datetime) or not isinstance(dt2, datetime.datetime):
        raise ValueError("Both arguments must be instances of datetime.datetime")
    
    return dt1.date() == dt2.date()

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 4, 15, 12, 30)
    dt2 = datetime.datetime(2023, 4, 15, 18, 45)
    print(compare_datetimes_ignoring_time(dt1, dt2))