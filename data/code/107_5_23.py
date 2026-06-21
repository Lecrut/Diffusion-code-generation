from datetime import datetime

def format_naive_datetime_to_tz_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    
    epoch = datetime(1970, 1, 1)
    delta = dt - epoch
    total_seconds = int(delta.total_seconds())
    
    is_negative = total_seconds < 0
    abs_seconds = abs(total_seconds)
    
    hours = abs_seconds // 3600
    remaining = abs_seconds % 3600
    minutes = remaining // 60
    
    sign = '-' if is_negative else '+'
    
    return f'{sign}{hours:02d}{minutes:02d}'

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = format_naive_datetime_to_tz_offset(sample_dt)
    print(result)