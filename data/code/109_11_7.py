import datetime
import calendar

def time_remaining_in_month(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    
    target_date = datetime.datetime(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end_date = datetime.datetime(year, month, last_day, 23, 59, 59)
    
    if year < current_year or (year == current_year and month < current_month):
        raise ValueError("The specified month and year must be in the future")
    
    if year == current_year and month == current_month:
        remaining_seconds = (end_date - now).total_seconds()
    else:
        remaining_seconds = (end_date - now).total_seconds()
    
    if remaining_seconds < 0:
        remaining_seconds = 0
    
    total_hours = int(remaining_seconds // 3600)
    remaining_minutes = int((remaining_seconds % 3600) // 60)
    remaining_seconds = int(remaining_seconds % 60)
    
    return {
        "hours": total_hours,
        "minutes": remaining_minutes,
        "seconds": remaining_seconds
    }

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)