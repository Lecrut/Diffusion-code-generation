def get_day_from_epoch(timestamp):
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    seconds_in_day = 86400
    days_since_epoch = timestamp // seconds_in_day
    
    year = 1970
    while True:
        days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365
        if days_since_epoch < days_in_year:
            break
        days_since_epoch -= days_in_year
        year += 1
    
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months_days[1] = 29
    
    month = 0
    while month < 12:
        if days_since_epoch < months_days[month]:
            break
        days_since_epoch -= months_days[month]
        month += 1
    
    day = days_since_epoch + 1
    return day

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1672531200]
    for ts in sample_timestamps:
        result = get_day_from_epoch(ts)
        print(result)