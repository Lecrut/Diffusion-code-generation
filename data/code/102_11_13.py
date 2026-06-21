import calendar

def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise TypeError("Input must be a string")
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if day < 1:
        raise ValueError("Invalid day")
    _, days_in_month = calendar.monthrange(year, month)
    if day > days_in_month:
        raise ValueError("Invalid day for month")
    weekday_index = calendar.weekday(year, month, day)
    return weekday_index < 5

if __name__ == '__main__':
    target_date = '2024-02-29'
    outcome = is_weekday(target_date)
    print(outcome)