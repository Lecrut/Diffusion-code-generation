import datetime
import time

def format_datetime_with_tz_offset(dt: datetime.datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive (no timezone info)')
    now = datetime.datetime.now()
    offset_seconds = time.timezone
    if time.daylight and time.localtime().tm_isdst > 0:
        offset_seconds = time.altzone
    if offset_seconds < 0:
        sign = '-'
        offset_seconds = abs(offset_seconds)
    else:
        sign = '+'
    hours = offset_seconds // 3600
    minutes = offset_seconds % 3600 // 60
    offset_str = f'{sign}{hours:02d}{minutes:02d}'
    dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return f'{dt_str}{offset_str}'
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = format_datetime_with_tz_offset(sample_dt)
    print(result)