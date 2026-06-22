import datetime

def format_datetime(dt_obj):
    if not isinstance(dt_obj, datetime.datetime):
        raise ValueError("Expected datetime object")
    hour = dt_obj.hour
    minute = dt_obj.minute
    second = dt_obj.second
    day = dt_obj.day
    month = dt_obj.month
    year = dt_obj.year
    
    period = "AM"
    if hour >= 12:
        period = "PM"
    
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12
    
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    hour_str = str(display_hour).zfill(2)
    minute_str = str(minute).zfill(2)
    second_str = str(second).zfill(2)
    
    return f"{day_str}/{month_str}/{year} {hour_str}:{minute_str}:{second_str} {period}"

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = format_datetime(sample_date)
    print(result)