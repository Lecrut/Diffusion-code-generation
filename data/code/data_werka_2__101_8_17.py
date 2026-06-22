import calendar
import datetime

def get_weekday_name(date_tuple):
    if not isinstance(date_tuple, (list, tuple)):
        raise TypeError("Input must be a sequence")
    if len(date_tuple) != 3:
        raise ValueError("Input must contain exactly three elements")
    year, month, day = date_tuple
    if not all(isinstance(v, int) for v in (year, month, day)):
        raise TypeError("Year, month, and day must be integers")
    try:
        datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError("Invalid date") from e
    index = calendar.weekday(year, month, day)
    return calendar.day_name[index]

if __name__ == '__main__':
    sample_date = (2024, 5, 15)
    result = get_weekday_name(sample_date)
    print(result)