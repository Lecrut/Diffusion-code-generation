from datetime import date
from typing import Tuple

COMPARISON_RESULTS: dict[int, int] = {
    1: 1,
    0: 0,
    -1: -1,
}

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Inputs must be datetime.date objects")
    if first > second:
        comparison_key: int = 1
    elif first < second:
        comparison_key: int = -1
    else:
        comparison_key: int = 0
    return COMPARISON_RESULTS[comparison_key]

if __name__ == '__main__':
    date_a: date = date(2025, 1, 1)
    date_b: date = date(2024, 12, 31)
    comparison_outcome: int = compare_dates(date_a, date_b)
    print(comparison_outcome)