from datetime import datetime, timedelta

def get_days_between(date_start: str, date_end: str) -> int:
    _validate_date_string(date_start)
    _validate_date_string(date_end)
    fmt = '%Y-%m-%d'
    d1 = datetime.strptime(date_start, fmt)
    d2 = datetime.strptime(date_end, fmt)
    return abs((d2 - d1).days)

def _validate_date_string(date_str: str) -> None:
    if not isinstance(date_str, str):
        raise TypeError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date must be in YYYY-MM-DD format")
    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Date components must have correct lengths")
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        raise ValueError("Date components must be digits")
    y, m, d = int(year), int(month), int(day)
    if m < 1 or m > 12:
        raise ValueError("Month out of range")
    if d < 1 or d > 31:
        raise ValueError("Day out of range")
    try:
        datetime(y, m, d)
    except ValueError as e:
        raise ValueError(f"Invalid date: {date_str}") from e

if __name__ == '__main__':
    val = get_days_between('2024-02-01', '2024-02-10')
    print(val)