from datetime import datetime

def validate_timezone_offset(offset):
    if not isinstance(offset, int) or offset < -1200 or offset > 1440:
        raise ValueError("Invalid timezone offset. Must be an integer between -1200 and 1440.")

def format_datetime_with_offset(dt):
    validate_timezone_offset(dt.utcoffset().total_seconds() // 60)
    return dt.strftime('%Y-%m-%d %H:%M:%S%z')[:-2]

if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 5, 14, 30)
    offset_dt = naive_dt.replace(tzinfo=timezone(timedelta(hours=3)))
    formatted_dt = format_datetime_with_offset(offset_dt)
    print(f"Input: {naive_dt}, Output: {formatted_dt}")