from datetime import datetime, timedelta, timezone

def format_naive_datetime_with_offset(dt: datetime, offset_hours: int) -> str:
    offset_minutes = offset_hours * 60
    sign = '+' if offset_minutes >= 0 else '-'
    abs_offset_minutes = abs(offset_minutes)
    hours = abs_offset_minutes // 60
    minutes = abs_offset_minutes % 60
    offset_str = f"{sign}{hours:02d}{minutes:02d}"
    return dt.strftime('%Y-%m-%dT%H:%M:%S') + offset_str

if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 5, 14, 30, 0)
    result = format_naive_datetime_with_offset(naive_dt, 5)
    print(result)
    
    result_negative = format_naive_datetime_with_offset(naive_dt, -4)
    print(result_negative)