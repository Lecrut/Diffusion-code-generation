import calendar

def get_weekday_name(date_tuple):
    if not isinstance(date_tuple, (list, tuple)):
        raise TypeError("Input must be a sequence of three integers")
    if len(date_tuple) != 3:
        raise ValueError("Input must contain exactly three elements")
    year, month, day = date_tuple
    if not all(isinstance(v, int) for v in (year, month, day)):
        raise TypeError("Year, month, and day must be integers")
    try:
        calendar.weekday(year, month, day)
    except OverflowError:
        raise ValueError("Date out of valid range")
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_date = (2023, 10, 25)
    result = get_weekday_name(sample_date)
    print(result)