from datetime import datetime
from typing import Union

DATE_FORMAT_MAP: dict[str, str] = {
    "iso": "%Y-%m-%dT%H:%M:%S",
    "date": "%Y-%m-%d",
    "time": "%H:%M:%S",
    "full": "%Y-%m-%dT%H:%M:%S.%f"
}

def _parse_date_string(date_str: str) -> datetime:
    for fmt in DATE_FORMAT_MAP.values():
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")

def find_earlier_date(date_str1: str, date_str2: str) -> datetime:
    dt1: datetime = _parse_date_string(date_str1)
    dt2: datetime = _parse_date_string(date_str2)
    if dt1 < dt2:
        return dt1
    return dt2

if __name__ == '__main__':
    result: datetime = find_earlier_date("2023-05-20T10:30:00", "2023-05-20T10:30:00")
    print(result)