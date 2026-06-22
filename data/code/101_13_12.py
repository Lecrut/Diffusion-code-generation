import datetime

def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    try:
        datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date provided")

def get_weekday_upper(year, month, day):
    validate_date(year, month, day)
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime('%A').upper()

if __name__ == '__main__':
    year = 2024
    month = 7
    day = 4
    result = get_weekday_upper(year, month, day)
    print(result)