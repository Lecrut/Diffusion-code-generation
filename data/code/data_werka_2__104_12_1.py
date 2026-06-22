from datetime import datetime
from typing import Tuple

DATE_FORMATS: dict[str, str] = {
    "standard": "%Y-%m-%dT%H:%M:%S",
    "date_only": "%Y-%m-%d",
    "with_tz": "%Y-%m-%dT%H:%M:%S%z"
}

def parse_iso_date(date_string: str) -> datetime:
    for fmt in DATE_FORMATS.values():
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {date_string}")

def get_earlier_iso_date(date_str1: str, date_str2: str) -> datetime:
    dt1 = parse_iso_date(date_str1)
    dt2 = parse_iso_date(date_str2)
    return dt1 if dt1 < dt2 else dt2

if __name__ == '__main__':
    earlier = get_earlier_iso_date("2023-10-01T12:00:00", "2023-10-02T12:00:00")
    print(earlier)