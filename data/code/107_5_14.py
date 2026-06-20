from datetime import datetime, timezone

def format_datetime_with_offset(dt):
    offset = dt.utcoffset()
    hours = abs(offset.total_seconds() // 3600)
    minutes = abs((offset.total_seconds() % 3600) // 60)
    sign = '+' if offset.days >= 0 else '-'
    return f"{dt.strftime('%Y-%m-%d %H:%M:%S')}{sign}{hours:02d}{minutes:02d}"

if __name__ == '__main__':
    dt = datetime(2023, 10, 5, 14, 30, tzinfo=timezone.utc)
    print(format_datetime_with_offset(dt))