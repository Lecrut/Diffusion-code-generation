from datetime import datetime, timezone
from typing import Optional

def parse_iso8601(date_string: str) -> datetime:
    cleaned = date_string.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    return datetime.fromisoformat(cleaned)

def determine_earlier_date(first_date: str, second_date: str) -> datetime:
    dt_first = parse_iso8601(first_date)
    dt_second = parse_iso8601(second_date)
    if dt_first.tzinfo is None:
        dt_first = dt_first.replace(tzinfo=timezone.utc)
    if dt_second.tzinfo is None:
        dt_second = dt_second.replace(tzinfo=timezone.utc)
    if dt_first < dt_second:
        return dt_first
    return dt_second

if __name__ == '__main__':
    date_a = "2024-05-20T14:30:00Z"
    date_b = "2024-05-20T14:30:00+05:30"
    earlier = determine_earlier_date(date_a, date_b)
    print(earlier.isoformat())