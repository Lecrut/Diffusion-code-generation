import calendar
import datetime

def get_weekday_name(date_tuple):
    if not isinstance(date_tuple, tuple) or len(date_tuple) != 3:
        raise ValueError("Input must be a tuple of three integers (year, month, day)")
    year, month, day = date_tuple
    for val in (year, month, day):
        if not isinstance(val, int):
            raise TypeError("Year, month, and day must be integers")
    try:
        datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    sample_date = (1999, 12, 31)
    result = get_weekday_name(sample_date)
    print(result)