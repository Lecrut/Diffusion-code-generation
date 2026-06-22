import datetime

def is_weekday(date_input):
    if isinstance(date_input, datetime.datetime):
        target_date = date_input.date()
    elif isinstance(date_input, datetime.date):
        target_date = date_input
    elif isinstance(date_input, str):
        parts = date_input.split("-")
        if len(parts) != 3:
            raise ValueError("Date string must be in YYYY-MM-DD format")
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except ValueError:
            raise ValueError("Date components must be integers")
        target_date = datetime.date(year, month, day)
    else:
        raise ValueError("Input must be a date, datetime, or date string")
    
    day_of_week = target_date.weekday()
    return day_of_week < 5

if __name__ == '__main__':
    sample_date_str = "2023-10-23"
    output = is_weekday(sample_date_str)
    print(output)