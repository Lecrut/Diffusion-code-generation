def parse_timestamp_to_date(timestamp: int) -> str:
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    days = timestamp // 86400
    remaining_seconds = timestamp % 86400
    
    year = 1970
    while True:
        days_in_year = 366 if _is_leap_year(year) else 365
        if days < days_in_year:
            break
        days -= days_in_year
        year += 1
    
    month_days = [31, 28 if _is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1
    while month <= 12:
        if days < month_days[month - 1]:
            break
        days -= month_days[month - 1]
        month += 1
    
    day = days + 1
    
    return f"{year:04d}/{month:02d}/{day:02d}"

def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1672531200]
    for ts in sample_timestamps:
        result = parse_timestamp_to_date(ts)
        print(result)