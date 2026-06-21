def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise TypeError("Expected a string")
    
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if day < 1:
        raise ValueError("Day out of range")
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        days_in_month[2] = 29
    
    if day > days_in_month[month]:
        raise ValueError("Day out of range for given month")
    
    if year < 1:
        raise ValueError("Year out of range")
    
    days_from_1970 = 0
    for y in range(1, year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days_from_1970 += 366
        else:
            days_from_1970 += 365
    
    for m in range(1, month):
        if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days_from_1970 += 29
        else:
            days_from_1970 += days_in_month[m]
    
    days_from_1970 += day
    
    weekday = (days_from_1970 + 3) % 7
    return weekday < 5

if __name__ == '__main__':
    sample_date = "2023-10-07"
    result = is_weekday(sample_date)
    print(result)