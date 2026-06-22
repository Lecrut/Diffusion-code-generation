from datetime import datetime
import calendar

def format_datetime(dt_obj):
    if not isinstance(dt_obj, datetime):
        raise ValueError("Input must be a datetime object")
    
    day = dt_obj.day
    month = dt_obj.month
    year = dt_obj.year
    hour = dt_obj.hour
    minute = dt_obj.minute
    
    period_map = {0: 'AM', 1: 'PM'}
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    period = period_map[hour // 12]
    
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    hour_str = f"{hour_12:02d}"
    minute_str = f"{minute:02d}"
    
    return f"{day_str}/{month_str}/{year_str} {hour_str}:{minute_str} {period}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime(sample_date)
    print(result)