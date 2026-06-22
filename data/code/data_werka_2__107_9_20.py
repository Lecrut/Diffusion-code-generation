import calendar

def format_date(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    
    parts = date_str.split('-')
    
    if len(parts) != 3:
        raise ValueError("Date string must contain exactly three parts separated by hyphens")
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    if day < 1:
        raise ValueError("Day must be positive")
    
    max_days = calendar.monthrange(year, month)[1]
    if day > max_days:
        raise ValueError(f"Day {day} is out of range for month {month} of year {year}")
    
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    print(format_date('2023-1-5'))
    print(format_date('2024-12-25'))
    print(format_date('2000-2-29'))