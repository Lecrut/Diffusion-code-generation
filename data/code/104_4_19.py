def validate_date_tuple(d):
    if not isinstance(d, (list, tuple)):
        raise ValueError("Input must be a tuple or list")
    if len(d) != 3:
        raise ValueError("Input must have exactly three elements")
    year, month, day = d
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Elements must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28
    else:
        max_day = days_in_month[month - 1]
    if day < 1 or day > max_day:
        raise ValueError("Day is out of range for the given month and year")
    return True

def is_same_calendar_date(date1, date2):
    validate_date_tuple(date1)
    validate_date_tuple(date2)
    return date1 == date2

if __name__ == '__main__':
    d1 = (2023, 10, 5)
    d2 = (2023, 10, 5)
    d3 = (2023, 10, 6)
    print(is_same_calendar_date(d1, d2))
    print(is_same_calendar_date(d1, d3))