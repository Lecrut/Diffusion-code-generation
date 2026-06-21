from datetime import datetime, date
from typing import Union

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

WEEKDAY_THRESHOLD = 5

def is_weekday(date_string: str) -> bool:
    parsed_date = datetime.fromisoformat(date_string).date()
    weekday_index = parsed_date.weekday()
    return weekday_index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    test_cases = [
        "2023-10-06",
        "2023-10-07",
        "2023-10-08",
        "2023-10-09",
        "2023-10-10",
        "2023-10-11",
        "2023-10-12",
    ]
    for date_str in test_cases:
        result = is_weekday(date_str)
        print(result)