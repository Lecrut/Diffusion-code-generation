import datetime
import locale

def format_datetime(dt_obj):
    if not isinstance(dt_obj, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    
    day = dt_obj.day
    month = dt_obj.month
    year = dt_obj.year
    hour = dt_obj.hour
    minute = dt_obj.minute
    
    period = "AM"
    if hour >= 12:
        period = "PM"
    
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12
    
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    hour_str = f"{display_hour:02d}"
    minute_str = f"{minute:02d}"
    
    return f"{day_str}/{month_str}/{year_str} {hour_str}:{minute_str} {period}"

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30)
    result = format_datetime(sample_dt)
    print(result)