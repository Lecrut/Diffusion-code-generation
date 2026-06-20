from datetime import datetime, timezone

def format_datetime_with_timezone(dt):
    return dt.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S+0000')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30)
    print(format_datetime_with_timezone(sample_dt))