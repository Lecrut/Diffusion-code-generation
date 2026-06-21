from datetime import datetime
from typing import Final

WEEKDAY_NAMES: Final[dict[int, str]] = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

WEEKDAY_BOUNDARY: Final[int] = 5

def is_weekday(date_string: str) -> bool:
    parsed_date = datetime.fromisoformat(date_string)
    weekday_index = parsed_date.weekday()
    return weekday_index < WEEKDAY_BOUNDARY

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