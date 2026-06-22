from datetime import datetime
from typing import Optional

class DateComparator:
    def __init__(self, first_date: datetime, second_date: datetime):
        self.first_date = first_date
        self.second_date = second_date

    def is_first_earlier(self) -> bool:
        if self.first_date < self.second_date:
            return True
        return False

def check_earliness(d1: datetime, d2: datetime) -> bool:
    if d1 is None or d2 is None:
        return False
    return d1 < d2

if __name__ == '__main__':
    first = datetime(2021, 11, 5, 10, 0, 0)
    second = datetime(2021, 11, 6, 10, 0, 0)
    comparator = DateComparator(first, second)
    print(comparator.is_first_earlier())
    print(check_earliness(first, second))