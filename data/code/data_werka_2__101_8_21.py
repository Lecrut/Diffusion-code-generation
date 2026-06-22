import calendar
import datetime

def _validate_date_tuple(date_tuple):
    if not isinstance(date_tuple, tuple):
        raise TypeError("Input must be a tuple")
    if len(date_tuple) != 3:
        raise ValueError("Tuple must contain exactly three elements")
    year, month, day = date_tuple
    if not all(isinstance(v, int) for v in (year, month, day)):
        raise TypeError("All elements must be integers")
    try:
        datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    return year, month, day

def get_weekday_name(date_tuple):
    year, month, day = _validate_date_tuple(date_tuple)
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    sample_date = (2023, 10, 25)
    result = get_weekday_name(sample_date)
    print(result)