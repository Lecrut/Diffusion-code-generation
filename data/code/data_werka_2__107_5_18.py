from datetime import datetime, timedelta, timezone

def format_naive_datetime_with_offset(dt: datetime, offset_hours: int, offset_minutes: int=0) -> str:
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    if not isinstance(offset_hours, int) or not isinstance(offset_minutes, int):
        raise ValueError('Offset components must be integers')
    total_offset_seconds = offset_hours * 3600 + offset_minutes * 60
    tz = timezone(timedelta(seconds=total_offset_seconds))
    aware_dt = dt.replace(tzinfo=tz)
    offset_str = aware_dt.strftime('%z')
    base_str = aware_dt.strftime('%Y-%m-%d %H:%M:%S')
    return f'{base_str} {offset_str}'
if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 27, 14, 30, 0)
    result = format_naive_datetime_with_offset(naive_dt, 5, 30)
    print(result)
    result_utc = format_naive_datetime_with_offset(naive_dt, 0, 0)
    print(result_utc)
    result_negative = format_naive_datetime_with_offset(naive_dt, -5, 0)
    print(result_negative)