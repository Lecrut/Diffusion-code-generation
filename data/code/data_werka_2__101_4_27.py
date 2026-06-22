from calendar import isleap

def get_day_of_week(date_string: str) -> int:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28
    
    if day < 1 or day > days_in_month[month]:
        raise ValueError("Day out of range for month")
    
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    total_days = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day)
    return total_days % 7

if __name__ == '__main__':
    print(get_day_of_week("2023-10-23"))
    print(get_day_of_week("2024-01-01"))
    print(get_day_of_week("2000-02-29"))