def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise TypeError('Input must be a string')
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError('Date string must be in YYYY-MM-DD format')
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError('Date components must be integers')
    if year < 1 or month < 1 or month > 12 or (day < 1):
        raise ValueError('Invalid date values')
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month[2] = 29
    if day > days_in_month[month]:
        raise ValueError('Invalid day for the given month and year')
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    dow = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7
    iso_weekday = (dow + 6) % 7
    return iso_weekday < 5
if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)