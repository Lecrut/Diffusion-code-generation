from datetime import date
from typing import Union

def compare_dates(first: date, second: date) -> int:
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    date1 = date(2023, 10, 1)
    date2 = date(2023, 10, 2)
    result = compare_dates(date1, date2)
    print(result)