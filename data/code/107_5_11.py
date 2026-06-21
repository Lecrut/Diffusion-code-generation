from datetime import datetime, timedelta

def format_naive_datetime_with_tz_offset(dt: datetime, offset_hours: int) -> str:
    offset_minutes = offset_hours * 60
    sign = '+' if offset_minutes >= 0 else '-'
    abs_offset_minutes = abs(offset_minutes)
    hours = abs_offset_minutes // 60
    minutes = abs_offset_minutes % 60
    tz_str = f"{sign}{hours:02d}{minutes:02d}"
    base_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return f"{base_str}{tz_str}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_naive_datetime_with_tz_offset(sample_dt, 5)
    print(result)
    
    sample_dt_negative = datetime(2023, 10, 5, 14, 30, 0)
    result_negative = format_naive_datetime_with_tz_offset(sample_dt_negative, -5)
    print(result_negative)