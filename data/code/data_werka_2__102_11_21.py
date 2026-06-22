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
    if year < 1:
        raise ValueError('Year must be positive')
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12')
    if day < 1:
        raise ValueError('Day must be positive')
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    if is_leap:
        days_in_month[2] = 29
    if day > days_in_month[month]:
        raise ValueError('Invalid day for the given month and year')
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h in (2, 3, 4, 5, 6)
if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)