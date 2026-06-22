def get_day_from_epoch(timestamp):
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    SECONDS_PER_DAY = 86400
    DAYS_PER_WEEK = 7
    DAYS_PER_MONTH = 30
    SECONDS_PER_MONTH = DAYS_PER_MONTH * SECONDS_PER_DAY
    
    total_days = timestamp // SECONDS_PER_DAY
    
    year = 1970
    while True:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_year = 366 if is_leap else 365
        
        if total_days < days_in_year:
            break
        
        total_days -= days_in_year
        year += 1
    
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = (31, 29 if is_leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    month_index = 0
    while month_index < 12:
        days_in_current_month = days_in_months[month_index]
        if total_days < days_in_current_month:
            break
        total_days -= days_in_current_month
        month_index += 1
    
    day_of_month = total_days + 1
    return day_of_month

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_from_epoch(sample_timestamp)
    print(result)