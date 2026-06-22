from datetime import datetime
import re

DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')

def validate_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Date string must be a string")
    if not DATE_PATTERN.match(date_str):
        raise ValueError(f"Invalid format for date string: {date_str}")
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        raise ValueError(f"Invalid date values: {e}")

def calculate_minutes_difference(date_str_1, date_str_2):
    validate_date_string(date_str_1)
    validate_date_string(date_str_2)
    fmt = '%Y-%m-%d %H:%M:%S'
    dt_1 = datetime.strptime(date_str_1, fmt)
    dt_2 = datetime.strptime(date_str_2, fmt)
    delta = dt_2 - dt_1
    total_seconds = delta.total_seconds()
    return total_seconds / 60

if __name__ == '__main__':
    start = '2023-01-01 10:00:00'
    end = '2023-01-01 12:30:00'
    diff = calculate_minutes_difference(start, end)
    print(diff)