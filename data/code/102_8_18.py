from datetime import datetime
from typing import Optional

WEEKDAY_LIMIT = 5

def is_weekday(date_string: str) -> bool:
    try:
        parsed_date = datetime.fromisoformat(date_string)
        return parsed_date.weekday() < WEEKDAY_LIMIT
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid date string provided: {date_string}") from exc

if __name__ == '__main__':
    sample_dates = [
        "2023-10-07",
        "2023-10-08",
        "2023-10-09",
        "2023-10-10",
        "2023-10-11"
    ]
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)