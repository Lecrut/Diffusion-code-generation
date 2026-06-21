import calendar

def validate_date_components(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Date components must be integers")
    if month < 1 or month > 12:
        raise ValueError(f"Month {month} is out of range")
    try:
        calendar.monthrange(year, month)
    except ValueError:
        raise ValueError(f"Day {day} is invalid for month {month} of year {year}")
    return True

def is_weekday(year, month, day):
    validate_date_components(year, month, day)
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    result = is_weekday(2023, 10, 23)
    print(result)
    result2 = is_weekday(2023, 10, 28)
    print(result2)