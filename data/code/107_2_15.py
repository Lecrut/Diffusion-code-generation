def parse_timestamp_to_date(timestamp: int) -> str:
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    days_since_epoch = timestamp // 86400
    remaining_seconds = timestamp % 86400
    
    year = 1970
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days_since_epoch < days_in_year:
            break
        days_since_epoch -= days_in_year
        year += 1
    
    month_days = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1
    for i, days in enumerate(month_days):
        if days_since_epoch < days:
            month = i + 1
            break
        days_since_epoch -= days
    
    day = days_since_epoch + 1
    
    return f"{year:04d}/{month:02d}/{day:02d}"

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1704067200]
    for ts in sample_timestamps:
        result = parse_timestamp_to_date(ts)
        print(result)