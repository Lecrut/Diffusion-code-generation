def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _days_in_month(year, month):
    month_map = {
        1: 31,
        2: 29 if _is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return month_map[month]

def format_timestamp_as_date(timestamp):
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    seconds_per_day = 86400
    days_since_epoch = timestamp // seconds_per_day
    
    year = 1970
    while True:
        days_in_current_year = 366 if _is_leap(year) else 365
        if days_since_epoch < days_in_current_year:
            break
        days_since_epoch -= days_in_current_year
        year += 1
        
    month = 1
    while month <= 12:
        days_in_current_month = _days_in_month(year, month)
        if days_since_epoch < days_in_current_month:
            break
        days_since_epoch -= days_in_current_month
        month += 1
        
    day = days_since_epoch + 1
    return f"{year:04d}/{month:02d}/{day:02d}"

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1546300800, 2147483647]
    for ts in sample_timestamps:
        result = format_timestamp_as_date(ts)
        print(result)