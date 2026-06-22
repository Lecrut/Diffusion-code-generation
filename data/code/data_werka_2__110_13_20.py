from datetime import datetime, timezone
from typing import List

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    if not date_strings:
        return []
    
    def parse_date(date_str: str) -> datetime:
        try:
            dt = datetime.fromisoformat(date_str)
            if dt.tzinfo is None:
                return dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid ISO 8601 date string: {date_str}")

    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    sample_dates = [
        "2023-10-01T12:00:00+00:00",
        "2021-05-15T08:30:00Z",
        "2023-01-01T00:00:00",
        "2022-12-31T23:59:59+05:30",
        "2020-02-29T10:00:00"
    ]
    sorted_result = sort_iso_dates(sample_dates)
    print(sorted_result)