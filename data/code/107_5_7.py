from datetime import datetime, timezone

def format_datetime_with_timezone(dt):
    offset = dt.utcoffset()
    if offset is None:
        return dt.isoformat() + '+0000'
    hours, remainder = divmod(offset.total_seconds() // 60, 60)
    minutes = remainder
    sign = '+' if hours >= 0 else '-'
    return dt.strftime('%Y-%m-%dT%H:%M:%S') + f'{sign}{hours:02d}{minutes:02d}'

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=timezone.utc)
    print(format_datetime_with_timezone(sample_dt))