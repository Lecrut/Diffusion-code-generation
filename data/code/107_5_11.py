from datetime import datetime, timezone

def format_datetime_with_offset(dt):
    offset = dt.utcoffset()
    if offset is None:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    hours, remainder = divmod(offset.total_seconds() / 3600, 1)
    minutes = int(remainder * 60)
    sign = '+' if offset.days >= 0 else '-'
    return f'{dt.strftime("%Y-%m-%d %H:%M:%S")}{sign}{int(hours):02}{minutes:02}'

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=timezone.utc)
    print(format_datetime_with_offset(sample_dt))