def get_day_from_epoch(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be an integer or float")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    seconds_in_day = 86400
    days_since_epoch = int(timestamp // seconds_in_day)
    
    year = 1970
    while True:
        days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365
        if days_since_epoch < days_in_year:
            break
        days_since_epoch -= days_in_year
        year += 1
    
    months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months_days[2] = 29
    
    month = 1
    while month <= 12:
        days_in_month = months_days[month]
        if days_since_epoch < days_in_month:
            break
        days_since_epoch -= days_in_month
        month += 1
    
    day = days_since_epoch + 1
    return day

if __name__ == '__main__':
    print(get_day_from_epoch(0))
    print(get_day_from_epoch(86400))
    print(get_day_from_epoch(1609459200))
    print(get_day_from_epoch(1704067200))