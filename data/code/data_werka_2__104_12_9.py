from datetime import datetime
from typing import Union

def _validate_iso_format(date_str: str) -> None:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) == 0:
        raise ValueError("Input string cannot be empty")
    if 'T' not in date_str:
        raise ValueError("ISO 8601 format requires 'T' separator")
    parts = date_str.split('T')
    if len(parts) != 2:
        raise ValueError("Invalid ISO 8601 structure")
    date_part = parts[0]
    time_part = parts[1]
    if len(date_part) != 10:
        raise ValueError("Date part must be YYYY-MM-DD")
    if len(time_part) < 8:
        raise ValueError("Time part must be at least HH:MM:SS")
    try:
        datetime.strptime(date_part, "%Y-%m-%d")
        datetime.strptime(time_part[:8], "%H:%M:%S")
    except ValueError:
        raise ValueError("Invalid date or time components")

def compare_iso_dates(date_str1: str, date_str2: str) -> str:
    _validate_iso_format(date_str1)
    _validate_iso_format(date_str2)
    dt1 = datetime.fromisoformat(date_str1)
    dt2 = datetime.fromisoformat(date_str2)
    if dt1 < dt2:
        return date_str1
    if dt2 < dt1:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = compare_iso_dates("2024-05-20T10:30:00", "2024-05-20T10:30:00")
    print(result)