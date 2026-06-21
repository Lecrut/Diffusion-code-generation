import datetime

def _validate_date_components(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    try:
        datetime.date(year, month, 1)
    except ValueError:
        raise ValueError("Invalid month for the given year")
    try:
        datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Day is out of range for the given month and year")
    return True

def get_day_of_week(year, month, day):
    _validate_date_components(year, month, day)
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)