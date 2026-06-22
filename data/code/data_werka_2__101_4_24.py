def get_day_of_week(date_string: str) -> int:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Date string must have three parts")
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    
    if len(parts[0]) != 4:
        raise ValueError("Year must have 4 digits")
    if len(parts[1]) != 2:
        raise ValueError("Month must have 2 digits")
    if len(parts[2]) != 2:
        raise ValueError("Day must have 2 digits")
        
    if year < 1:
        raise ValueError("Year must be positive")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
        
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    days_in_month = [0, 31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day > days_in_month[month]:
        raise ValueError(f"Day {day} out of range for month {month} in year {year}")
        
    import calendar
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    print(get_day_of_week("2023-10-23"))
    print(get_day_of_week("2024-01-01"))
    print(get_day_of_week("2000-02-29"))