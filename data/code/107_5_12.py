import datetime
import time

def format_datetime_with_tz_offset(dt: datetime.datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive (no timezone info)')
    now = datetime.datetime.now()
    offset_seconds = time.timezone if not time.daylight else time.altzone
    offset_hours, offset_seconds = divmod(abs(offset_seconds), 3600)
    offset_minutes = offset_seconds // 60
    sign = '+' if offset_seconds >= 0 else '-'
    offset_str = f'{sign}{offset_hours:02d}{offset_minutes:02d}'
    return dt.strftime('%Y-%m-%d %H:%M:%S') + offset_str
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = format_datetime_with_tz_offset(sample_dt)
    print(result)