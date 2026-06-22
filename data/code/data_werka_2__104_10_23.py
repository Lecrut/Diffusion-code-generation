from datetime import date
from typing import Any

LATER: int = 1
EARLIER: int = 0
EQUAL: int = -1
OFFSET_VALUE: int = 1
BASE_COMPARISON: int = 0
SECOND_DATE_INDEX: int = 1

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Both inputs must be instances of datetime.date")
    first_int: int = first.toordinal()
    second_int: int = second.toordinal()
    raw_comparison: int = BASE_COMPARISON if first_int == second_int else LATER if first_int > second_int else EARLIER
    return raw_comparison * OFFSET_VALUE if raw_comparison else raw_comparison

if __name__ == '__main__':
    date_a: date = date(2024, 1, 1)
    date_b: date = date(2023, 12, 31)
    comparison_result: int = compare_dates(date_a, date_b)
    print(comparison_result)