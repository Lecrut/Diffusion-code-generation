from datetime import datetime, timedelta, timezone

def format_naive_datetime_with_offset(dt: datetime, offset_hours: int, offset_minutes: int) -> str:
    sign = '+' if offset_hours >= 0 and offset_minutes >= 0 or (offset_hours < 0 and offset_minutes < 0) else '-'
    abs_offset_hours = abs(offset_hours)
    abs_offset_minutes = abs(offset_minutes)
    offset_str = f'{sign}{abs_offset_hours:02d}{abs_offset_minutes:02d}'
    dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return f'{dt_str}{offset_str}'
if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 27, 14, 30, 0)
    result = format_naive_datetime_with_offset(naive_dt, 5, 30)
    print(result)
    naive_dt_negative = datetime(2023, 10, 27, 14, 30, 0)
    result_negative = format_naive_datetime_with_offset(naive_dt_negative, -4, 0)
    print(result_negative)