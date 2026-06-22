def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def _days_in_month(year: int, month: int) -> int:
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and _is_leap_year(year):
        return 29
    return days[month]

def _validate_date_string(date_string: str) -> tuple:
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
    max_day = _days_in_month(year, month)
    if day > max_day:
        raise ValueError(f'Day {day} is out of range for month {month} in year {year}')
    return year, month, day

def _day_of_week(year: int, month: int, day: int) -> int:
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return (h + 5) % 7

def is_weekday(date_string: str) -> bool:
    year, month, day = _validate_date_string(date_string)
    weekday = _day_of_week(year, month, day)
    return 0 <= weekday <= 4

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)