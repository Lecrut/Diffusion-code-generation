from datetime import datetime, timedelta, timezone

OFFSET_MAP = {
    'UTC': 0,
    'EST': -5,
    'PST': -8,
    'IST': 5.5,
    'CET': 1,
    'JST': 9,
}

def format_naive_datetime_with_tz(dt: datetime, tz_name: str) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    
    if tz_name not in OFFSET_MAP:
        raise ValueError(f'Unsupported timezone: {tz_name}')
    
    offset_hours = OFFSET_MAP[tz_name]
    total_seconds = int(offset_hours * 3600)
    
    if total_seconds < 0:
        sign = '-'
        total_seconds = abs(total_seconds)
    else:
        sign = '+'
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    
    dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return f'{dt_str}{sign}{hours:02d}{minutes:02d}'

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = format_naive_datetime_with_tz(sample_dt, 'IST')
    print(result)
    result_pst = format_naive_datetime_with_tz(sample_dt, 'PST')
    print(result_pst)