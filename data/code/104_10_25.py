from datetime import date
from typing import Tuple

def compare_dates(first: date, second: date) -> int:
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    d1: date = date(2024, 1, 1)
    d2: date = date(2024, 1, 1)
    print(compare_dates(d1, d2))