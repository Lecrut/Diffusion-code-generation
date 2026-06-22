def extract_day_from_epoch(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be an integer or float")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    seconds_in_day = 86400
    days_since_epoch = int(timestamp // seconds_in_day)
    
    year = 1970
    while True:
        days_in_current_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365
        if days_since_epoch < days_in_current_year:
            break
        days_since_epoch -= days_in_current_year
        year += 1
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[1] = 29
    
    month = 0
    while month < 12:
        if days_since_epoch < month_days[month]:
            break
        days_since_epoch -= month_days[month]
        month += 1
    
    day = days_since_epoch + 1
    return day

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1640995200]
    for ts in sample_timestamps:
        result = extract_day_from_epoch(ts)
        print(result)