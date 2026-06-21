from datetime import datetime, timezone, timedelta

def format_rfc2822(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    if dt.tzinfo is not None:
        offset_seconds = dt.utcoffset().total_seconds()
        offset_hours = int(offset_seconds // 3600)
        offset_minutes = int((offset_seconds % 3600) // 60)
        sign = "+" if offset_hours >= 0 else "-"
        tz_str = f"{sign}{abs(offset_hours):02d}{abs(offset_minutes):02d}"
    else:
        dt_utc = dt.replace(tzinfo=timezone.utc)
        offset_seconds = dt_utc.utcoffset().total_seconds()
        offset_hours = int(offset_seconds // 3600)
        offset_minutes = int((offset_seconds % 3600) // 60)
        sign = "+" if offset_hours >= 0 else "-"
        tz_str = f"{sign}{abs(offset_hours):02d}{abs(offset_minutes):02d}"
    
    day_abbr = dt.strftime("%a")
    day = dt.day
    month_abbr = dt.strftime("%b")
    year = dt.year
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    
    return f"{day_abbr}, {day:02d} {month_abbr} {year} {hour:02d}:{minute:02d}:{second:02d} {tz_str}"

if __name__ == '__main__':
    utc_dt = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    print(format_rfc2822(utc_dt))
    
    naive_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(format_rfc2822(naive_dt))
    
    offset_dt = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone(timedelta(hours=5, minutes=30)))
    print(format_rfc2822(offset_dt))