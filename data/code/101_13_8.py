import datetime

def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Year, month, and day must be integers")
    if year < 1 or year > 9999:
        raise ValueError("Year out of range")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    try:
        datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date for the given month/year")

def get_weekday(year, month, day):
    validate_date(year, month, day)
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime('%A').upper()

if __name__ == '__main__':
    year = 2024
    month = 7
    day = 4
    result = get_weekday(year, month, day)
    print(result)