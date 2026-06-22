def get_day_of_month(timestamp: int) -> int:
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    
    SECONDS_PER_DAY = 86400
    DAYS_SINCE_EPOCH = timestamp // SECONDS_PER_DAY
    
    year = 1970
    while True:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_year = 366
        else:
            days_in_year = 365
            
        if DAYS_SINCE_EPOCH < days_in_year:
            break
            
        DAYS_SINCE_EPOCH -= days_in_year
        year += 1
        
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        month_lengths[1] = 29
        
    month_index = 0
    while month_index < 12:
        if DAYS_SINCE_EPOCH < month_lengths[month_index]:
            break
        DAYS_SINCE_EPOCH -= month_lengths[month_index]
        month_index += 1
        
    day_of_month = DAYS_SINCE_EPOCH + 1
    return day_of_month

if __name__ == '__main__':
    sample_timestamp = 1700000000
    result = get_day_of_month(sample_timestamp)
    print(result)