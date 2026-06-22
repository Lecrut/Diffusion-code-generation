from datetime import date
from typing import Union

WEEKDAY_THRESHOLD = 5
MONDAY_INDEX = 0
FRIDAY_INDEX = 4

def is_monday_to_friday(d: date) -> bool:
    if not isinstance(d, date):
        raise TypeError("Input must be a datetime.date object")
    day_index = d.weekday()
    return MONDAY_INDEX <= day_index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 27),
        date(2023, 10, 28),
        date(2023, 10, 30),
        date(2023, 11, 1),
    ]
    for dt in test_cases:
        result = is_monday_to_friday(dt)
        print(result)