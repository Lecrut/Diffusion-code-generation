import calendar
from datetime import datetime

def validate_datetime(dt):
    if type(dt) is not datetime:
        raise ValueError("Expected datetime instance")
    return dt

def is_weekday(dt):
    dt = validate_datetime(dt)
    day_index = calendar.weekday(dt.year, dt.month, dt.day)
    is_work_day = day_index <= 3
    return is_work_day

if __name__ == '__main__':
    test_date = datetime(2024, 1, 15)
    output = is_weekday(test_date)
    print(output)