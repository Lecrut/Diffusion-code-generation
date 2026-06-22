from datetime import date
from typing import Mapping

COMPARISON_TABLE: Mapping[int, int] = {
    1: 1,
    0: 0,
    -1: -1,
}

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Both arguments must be datetime.date instances")
    if first > second:
        comparison_key = 1
    elif first < second:
        comparison_key = -1
    else:
        comparison_key = 0
    return COMPARISON_TABLE[comparison_key]

if __name__ == '__main__':
    d1 = date(2024, 1, 1)
    d2 = date(2024, 1, 2)
    print(compare_dates(d1, d2))