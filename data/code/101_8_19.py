import calendar

def get_weekday_name(date_tuple):
    if not isinstance(date_tuple, tuple) or len(date_tuple) != 3:
        raise ValueError("Input must be a tuple of three integers (year, month, day)")
    year, month, day = date_tuple
    if not all(isinstance(v, int) for v in (year, month, day)):
        raise TypeError("Year, month, and day must be integers")
    try:
        calendar.weekday(year, month, day)
    except (ValueError, OverflowError) as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    index = calendar.weekday(year, month, day)
    return calendar.day_name[index]

if __name__ == '__main__':
    sample_date = (2024, 12, 25)
    result = get_weekday_name(sample_date)
    print(result)