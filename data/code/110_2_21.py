from datetime import datetime
from typing import List

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    def parse_date(date_str: str) -> float:
        try:
            dt = datetime.fromisoformat(date_str)
            return dt.timestamp()
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid ISO 8601 date string: {date_str}") from e

    sorted_dates = sorted(date_strings, key=parse_date)
    return sorted_dates

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-01-15T08:30:00",
        "2024-05-20T18:45:00",
        "2022-12-31T23:59:59",
        "2023-02-28T14:15:00"
    ]
    result = sort_iso_dates(dates)
    print(result)