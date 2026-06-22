import datetime
import os

def calculate_date_delta(start: datetime.date, end: datetime.date) -> int:
    delta = end - start
    return delta.days

def calculate_timedelta_with_dst(start_dt: datetime.datetime, end_dt: datetime.datetime) -> datetime.timedelta:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        raise ValueError("Timezone-aware datetimes are required for DST handling.")
    start_utc = start_dt.astimezone(datetime.timezone.utc)
    end_utc = end_dt.astimezone(datetime.timezone.utc)
    return end_utc - start_utc

def get_current_utc_timestamp() -> int:
    return int(datetime.datetime.now(datetime.timezone.utc).timestamp())

if __name__ == '__main__':
    date_start = datetime.date(2024, 2, 15)
    date_end = datetime.date(2024, 3, 10)
    days_count = calculate_date_delta(date_start, date_end)
    print(days_count)

    tz_ny = datetime.timezone(datetime.timedelta(hours=-5))
    tz_london = datetime.timezone(datetime.timedelta(hours=0))

    dt_start = datetime.datetime(2024, 3, 10, 12, 0, 0, tzinfo=tz_ny)
    dt_end = datetime.datetime(2024, 3, 10, 12, 0, 0, tzinfo=tz_london)
    time_delta = calculate_timedelta_with_dst(dt_start, dt_end)
    print(time_delta.total_seconds())

    utc_ts = get_current_utc_timestamp()
    print(utc_ts)