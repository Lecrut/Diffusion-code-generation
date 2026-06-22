def get_day_of_month(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a number')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    
    total_seconds = int(timestamp)
    total_days = total_seconds // 86400
    
    year = 1970
    while True:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_year = 366 if is_leap else 365
        if total_days < days_in_year:
            break
        total_days -= days_in_year
        year += 1
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
        
    month = 1
    while month < 12:
        if total_days < month_days[month - 1]:
            break
        total_days -= month_days[month - 1]
        month += 1
        
    day = total_days + 1
    return day

if __name__ == '__main__':
    print(get_day_of_month(1672531200))
    print(get_day_of_month(0))
    print(get_day_of_month(1609459200))