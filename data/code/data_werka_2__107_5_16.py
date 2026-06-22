import datetime
import time

def format_datetime_with_tz_offset(dt: datetime.datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive (no timezone info)')
    offset_seconds = time.altzone if time.daylight and time.localtime().tm_isdst else time.timezone
    offset_hours = offset_seconds // 3600
    offset_minutes = abs(offset_seconds) % 3600 // 60
    sign = '+' if offset_seconds <= 0 else '-'
    if time.daylight and time.localtime().tm_isdst:
        offset_seconds = -time.altzone
    else:
        offset_seconds = -time.timezone
    offset_hours = offset_seconds // 3600
    offset_minutes = abs(offset_seconds) % 3600 // 60
    sign = '+' if offset_seconds >= 0 else '-'
    return f"{dt.strftime('%Y-%m-%d %H:%M:%S')}{sign}{abs(offset_hours):02d}{offset_minutes:02d}"
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = format_datetime_with_tz_offset(sample_dt)
    print(result)