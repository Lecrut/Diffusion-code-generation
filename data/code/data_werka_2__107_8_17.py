import datetime

def format_datetime(dt_obj):
    if not isinstance(dt_obj, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    hour = dt_obj.hour
    period = "AM"
    if hour >= 12:
        period = "PM"
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12
    return f"{dt_obj.day:02d}/{dt_obj.month:02d}/{dt_obj.year} {display_hour:02d}:{dt_obj.minute:02d} {period}"

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30, 0)
    result = format_datetime(sample_date)
    print(result)