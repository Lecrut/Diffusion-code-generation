import calendar

def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Year, month, and day must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    try:
        calendar.monthrange(year, month)
    except ValueError:
        raise ValueError("Invalid day for the given month and year")
    return True

def get_weekday_name(year, month, day):
    validate_date(year, month, day)
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    result = get_weekday_name(year, month, day)
    print(result)