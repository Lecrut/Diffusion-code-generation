import datetime
import calendar

def is_weekday(date_input):
    if isinstance(date_input, datetime.datetime):
        date_obj = date_input.date()
    elif isinstance(date_input, datetime.date):
        date_obj = date_input
    elif isinstance(date_input, str):
        parts = date_input.split("-")
        if len(parts) != 3:
            raise ValueError("Date string must be in YYYY-MM-DD format")
        try:
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        except ValueError:
            raise ValueError("Date components must be integers")
        try:
            calendar.timegm((year, month, day, 0, 0, 0))
            date_obj = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date values")
    else:
        raise ValueError("Input must be a date string, datetime.date, or datetime.datetime object")
    
    return date_obj.weekday() < 5

if __name__ == '__main__':
    test_date = datetime.date(2023, 10, 23)
    print(is_weekday(test_date))