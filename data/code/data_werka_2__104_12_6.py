from datetime import datetime, timezone
from typing import Optional

DATE_FORMATS: dict[str, str] = {
    "with_microseconds": "%Y-%m-%dT%H:%M:%S.%f",
    "with_timezone": "%Y-%m-%dT%H:%M:%S%z",
    "standard": "%Y-%m-%dT%H:%M:%S"
}

def _parse_date(date_str: str) -> datetime:
    for fmt in DATE_FORMATS.values():
        try:
            dt = datetime.strptime(date_str, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    raise ValueError(f"Invalid ISO 8601 format: {date_str}")

def get_earlier_iso_date(date_str1: str, date_str2: str) -> datetime:
    dt1 = _parse_date(date_str1)
    dt2 = _parse_date(date_str2)
    return dt1 if dt1 < dt2 else dt2

if __name__ == '__main__':
    result = get_earlier_iso_date("2023-10-01T12:00:00", "2023-10-02T12:00:00")
    print(result)