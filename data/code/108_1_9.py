def get_day_of_month(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a number')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    
    SECONDS_PER_DAY = 86400
    DAYS_PER_WEEK = 7
    DAYS_IN_COMMON_YEAR = 365
    DAYS_IN_LEAP_YEAR = 366
    LEAP_CYCLE_DAYS = 146097
    
    total_seconds = int(timestamp)
    total_days = total_seconds // SECONDS_PER_DAY
    
    year = 1970
    remaining_days = total_days
    
    if remaining_days >= LEAP_CYCLE_DAYS:
        cycles, remaining_days = divmod(remaining_days, LEAP_CYCLE_DAYS)
        year += cycles * 400
    
    while True:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_current_year = DAYS_IN_LEAP_YEAR if is_leap else DAYS_IN_COMMON_YEAR
        
        if remaining_days < days_in_current_year:
            break
        
        remaining_days -= days_in_current_year
        year += 1
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        month_days[1] = 29
    
    month = 1
    while month <= 12:
        days_in_month = month_days[month - 1]
        if remaining_days < days_in_month:
            break
        remaining_days -= days_in_month
        month += 1
    
    day = remaining_days + 1
    return day

if __name__ == '__main__':
    print(get_day_of_month(1672531200))
    print(get_day_of_month(0))
    print(get_day_of_month(1609459200))