from datetime import datetime, timedelta, timezone

def format_datetime_with_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    utc_dt = dt.replace(tzinfo=timezone.utc)
    offset = utc_dt.utcoffset()
    total_seconds = int(offset.total_seconds())
    if total_seconds < 0:
        sign = '-'
        total_seconds = -total_seconds
    else:
        sign = '+'
    hours = total_seconds // 3600
    minutes = total_seconds % 3600 // 60
    return f'{sign}{hours:02d}{minutes:02d}'
if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime_with_offset(naive_dt)
    print(result)