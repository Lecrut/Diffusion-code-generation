def determine_day(timestamp):
    if not isinstance(timestamp, int) or timestamp < 1000000:
        raise ValueError("Invalid input: Timestamp must be an integer with at least 7 digits.")
    
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    
    if month < 1 or month > 12:
        raise ValueError("Invalid input: Month must be between 1 and 12.")
    
    if day < 1:
        raise ValueError("Invalid input: Day must be greater than 0.")
    
    if month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap_year else 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    
    if day > max_day:
        raise ValueError("Invalid input: Day out of range for the given month.")
    
    return day

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {determine_day(timestamp1)}")
    
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {determine_day(timestamp2)}")
    
    timestamp3 = 20240229
    try:
        print(f"The day for {timestamp3} is: {determine_day(timestamp3)}")
    except ValueError as e:
        print(e)