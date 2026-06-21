from datetime import date
from typing import Final

class DateComparator:
    LATER: Final[int] = 1
    EARLIER: Final[int] = -1
    EQUAL: Final[int] = 0

    def compare(self, first: date, second: date) -> int:
        if not isinstance(first, date) or not isinstance(second, date):
            raise ValueError("Arguments must be datetime.date instances")
        if first > second:
            return self.LATER
        if first < second:
            return self.EARLIER
        return self.EQUAL

if __name__ == '__main__':
    comparator = DateComparator()
    d_a = date(2025, 1, 1)
    d_b = date(2024, 12, 31)
    d_c = date(2025, 1, 1)
    res1 = comparator.compare(d_a, d_b)
    res2 = comparator.compare(d_b, d_a)
    res3 = comparator.compare(d_a, d_c)
    print(res1)
    print(res2)
    print(res3)