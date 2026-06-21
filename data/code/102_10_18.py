import calendar
from datetime import datetime

def validate_datetime_input(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    return dt

def is_weekday(dt):
    validated_dt = validate_datetime_input(dt)
    day_index = calendar.weekday(validated_dt.year, validated_dt.month, validated_dt.day)
    return day_index < 5

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)