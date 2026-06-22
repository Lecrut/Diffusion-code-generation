from datetime import date
from typing import Final

class DateComparator:
    LATER: Final[int] = 1
    EARLIER: Final[int] = -1
    EQUAL: Final[int] = 0

    @staticmethod
    def compare(first: date, second: date) -> int:
        if not isinstance(first, date) or not isinstance(second, date):
            raise ValueError("Arguments must be datetime.date instances")
        if first > second:
            return DateComparator.LATER
        if first < second:
            return DateComparator.EARLIER
        return DateComparator.EQUAL

if __name__ == '__main__':
    d1 = date(2024, 1, 1)
    d2 = date(2024, 1, 2)
    val = DateComparator.compare(d1, d2)
    print(val)