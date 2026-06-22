from datetime import datetime, timedelta, timezone

def format_datetime_with_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive (no timezone info)')
    utc_dt = dt.replace(tzinfo=timezone.utc)
    offset = utc_dt.utcoffset()
    total_seconds = int(offset.total_seconds())
    if total_seconds < 0:
        sign = '-'
        total_seconds = abs(total_seconds)
    else:
        sign = '+'
    hours = total_seconds // 3600
    minutes = total_seconds % 3600 // 60
    return f'{sign}{hours:02d}{minutes:02d}'
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = format_datetime_with_offset(sample_dt)
    print(result)