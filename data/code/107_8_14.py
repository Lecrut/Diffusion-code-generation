import datetime

HOUR_CYCLE = 12
ZERO_HOUR_DISPLAY = 12
SEPARATOR = ":"
SPACE = " "

def format_datetime(dt_obj: datetime.datetime) -> str:
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
    
    display_hour = hour % HOUR_CYCLE
    if display_hour == 0:
        display_hour = ZERO_HOUR_DISPLAY
    
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    hour_str = f"{display_hour:02d}"
    minute_str = f"{minute:02d}"
    
    time_part = f"{hour_str}{SEPARATOR}{minute_str}{SPACE}{period}"
    date_part = f"{day_str}/{month_str}/{year}"
    
    return f"{date_part} {time_part}"

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime(sample_date)
    print(result)