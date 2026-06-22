import datetime
import time

def calculate_date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def calculate_datetime_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        naive_start = start_dt.replace(tzinfo=datetime.timezone.utc) if start_dt.tzinfo is None else start_dt
        naive_end = end_dt.replace(tzinfo=datetime.timezone.utc) if end_dt.tzinfo is None else end_dt
        delta = naive_end - naive_start
    else:
        delta = end_dt - start_dt
    return delta.total_seconds()

if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 12, 31)
    days_diff = calculate_date_difference(date1, date2)
    print(days_diff)

    dt1 = datetime.datetime(2023, 3, 10, 1, 0, 0)
    dt2 = datetime.datetime(2023, 3, 10, 3, 0, 0)
    seconds_diff = calculate_datetime_difference(dt1, dt2)
    print(seconds_diff)

    tz = datetime.timezone(datetime.timedelta(hours=-5))
    dt_tz1 = datetime.datetime(2023, 11, 5, 0, 0, 0, tzinfo=tz)
    dt_tz2 = datetime.datetime(2023, 11, 5, 1, 0, 0, tzinfo=tz)
    tz_seconds_diff = calculate_datetime_difference(dt_tz1, dt_tz2)
    print(tz_seconds_diff)