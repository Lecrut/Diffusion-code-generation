import calendar

def validate_date_tuple(date_tuple):
    if not isinstance(date_tuple, (list, tuple)):
        raise TypeError("Input must be a sequence")
    if len(date_tuple) != 3:
        raise ValueError("Sequence must contain exactly three elements")
    year, month, day = date_tuple
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("All elements must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    return year, month, day

def get_weekday_name(date_tuple):
    year, month, day = validate_date_tuple(date_tuple)
    index = calendar.weekday(year, month, day)
    return calendar.day_name[index]

if __name__ == '__main__':
    sample_date = (2023, 10, 25)
    result = get_weekday_name(sample_date)
    print(result)