from datetime import datetime
import re

def _validate_iso_format(date_str: str) -> bool:
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'
    return bool(re.match(pattern, date_str))

def _parse_iso_date(date_str: str) -> datetime:
    if not _validate_iso_format(date_str):
        raise ValueError(f"Invalid ISO 8601 format: {date_str}")
    try:
        return datetime.fromisoformat(date_str)
    except ValueError as e:
        raise ValueError(f"Failed to parse date: {date_str}") from e

def find_earlier_iso_date(date_str1: str, date_str2: str) -> str:
    dt1 = _parse_iso_date(date_str1)
    dt2 = _parse_iso_date(date_str2)
    if dt1 < dt2:
        return date_str1
    if dt2 < dt1:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = find_earlier_iso_date("2023-05-15T10:30:00Z", "2023-05-15T10:30:00+05:00")
    print(result)