from datetime import datetime, timedelta, timezone

def format_naive_datetime_with_tz_offset(dt: datetime) -> str:
    if dt.tzinfo is not None:
        raise ValueError('Input datetime must be naive')
    local_epoch = datetime(1970, 1, 1)
    naive_delta = dt - local_epoch
    total_seconds = int(naive_delta.total_seconds())
    hours_offset = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes_offset = remaining_seconds // 60
    sign = '+' if hours_offset >= 0 else '-'
    abs_hours = abs(hours_offset)
    return f"{sign}{abs_hours:02d}{minutes_offset:02d}"

if __name__ == '__main__':
    sample_naive_dt = datetime(2024, 1, 15, 10, 0, 0)
    output = format_naive_datetime_with_tz_offset(sample_naive_dt)
    print(output)