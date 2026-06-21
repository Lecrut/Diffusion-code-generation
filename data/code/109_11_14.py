import datetime
import calendar

def time_remaining_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    now = datetime.datetime.now()
    
    if now.year > year or (now.year == year and now.month > month):
        raise ValueError("The specified month has already passed")
    
    start_of_month = datetime.datetime(year, month, 1, 0, 0, 0)
    
    if now.year == year and now.month == month:
        end_of_month = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    else:
        end_of_month = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    
    delta = end_of_month - now
    
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0:
        total_seconds = 0
    
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    
    result = time_remaining_in_month(current_year, current_month)
    print(result)