from datetime import datetime
from typing import Optional

WEEKDAY_LIMIT = 5

def is_weekday(date_string: str) -> bool:
    parsed = datetime.fromisoformat(date_string)
    return parsed.weekday() < WEEKDAY_LIMIT

if __name__ == '__main__':
    test_dates = [
        "2023-10-06",
        "2023-10-07",
        "2023-10-08",
        "2023-10-09",
        "2023-10-10",
        "2023-10-11",
        "2023-10-12"
    ]
    results = [is_weekday(d) for d in test_dates]
    for date_str, result in zip(test_dates, results):
        print(f"{date_str}: {result}")