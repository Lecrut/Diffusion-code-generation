from datetime import datetime, timezone

def format_datetime_with_timezone(dt):
    offset = dt.utcoffset()
    if offset:
        hours, remainder = divmod(offset.total_seconds() / 3600, 1)
        minutes = int(remainder * 60)
        return f"{dt.strftime('%Y-%m-%d %H:%M:%S')}+{int(hours):02}{minutes:02}"
    else:
        return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=timezone.utc)
    print(format_datetime_with_timezone(sample_dt))