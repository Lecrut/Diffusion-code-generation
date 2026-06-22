from datetime import datetime, timezone
from typing import Tuple

def _validate_iso_format(date_string: str) -> None:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if not date_string:
        raise ValueError("Input string cannot be empty")
    if 'T' not in date_string and '-' not in date_string:
        raise ValueError("Invalid ISO 8601 format")

def parse_iso_date(date_string: str) -> datetime:
    _validate_iso_format(date_string)
    try:
        return datetime.fromisoformat(date_string)
    except ValueError:
        raise ValueError(f"Failed to parse date: {date_string}")

def get_earlier_iso_date(date_str1: str, date_str2: str) -> str:
    dt1 = parse_iso_date(date_str1)
    dt2 = parse_iso_date(date_str2)
    if dt1 < dt2:
        return date_str1
    if dt2 < dt1:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = get_earlier_iso_date("2024-05-20T10:00:00", "2024-05-21T10:00:00")
    print(result)