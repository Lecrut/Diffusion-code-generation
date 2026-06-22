from datetime import date

def format_custom_date(y, m, d):
    if m < 1 or m > 12:
        raise ValueError("Month must be between 1 and 12")
    if d < 1 or d > 31:
        raise ValueError("Day must be between 1 and 31")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    try:
        dt = date(y, m, d)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}") from e
        
    day_name = days[dt.weekday()]
    month_name = months[dt.month - 1]
    
    return f"{day_name}, {month_name} {dt.day:02d}, {dt.year}"

if __name__ == '__main__':
    result = format_custom_date(2023, 10, 25)
    print(result)