def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise TypeError('Input must be a string')
    if len(date_string) != 10:
        raise ValueError('Invalid date string length')
    if date_string[4] != '-' or date_string[7] != '-':
        raise ValueError('Invalid date format')
    try:
        year = int(date_string[:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
    except ValueError:
        raise ValueError('Date components must be integers')
    if month < 1 or month > 12:
        raise ValueError('Invalid month')
    if day < 1:
        raise ValueError('Invalid day')
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    if is_leap:
        days_in_months[2] = 29
    if day > days_in_months[month]:
        raise ValueError('Invalid day for month')
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = year
    if month < 3:
        y -= 1
    day_of_week = (y + y // 4 - y // 100 + y // 400 + t[month - 1] + day) % 7
    return 1 <= day_of_week <= 5
if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)