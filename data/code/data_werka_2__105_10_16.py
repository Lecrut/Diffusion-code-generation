from datetime import datetime, timedelta
import calendar

def get_next_day(date_str: str) -> datetime:
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    
    parts = date_str.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
        
    max_days = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_days:
        raise ValueError("Invalid day for month")

    if day < max_days:
        next_day = day + 1
        next_month = month
        next_year = year
    else:
        next_day = 1
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
            
    return datetime(next_year, next_month, next_day)

if __name__ == '__main__':
    sample_date = '2024-02-28'
    result = get_next_day(sample_date)
    print(result)