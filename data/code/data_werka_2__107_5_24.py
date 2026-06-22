from datetime import datetime, timedelta, timezone

def format_datetime_with_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    offset_minutes = 330
    total_seconds = offset_minutes * 60
    sign = '+' if total_seconds >= 0 else '-'
    abs_seconds = abs(total_seconds)
    hours = abs_seconds // 3600
    minutes = abs_seconds % 3600 // 60
    offset_str = f'{sign}{hours:02d}{minutes:02d}'
    dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S')
    return f'{dt_str}{offset_str}'
if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime_with_offset(naive_dt)
    print(result)