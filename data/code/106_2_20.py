from datetime import datetime
from typing import Tuple

class YearSpanCalculator:
    _MIN_YEAR_DIFF = 0
    _YEAR_CORRECTION = 1

    def __init__(self, start: datetime, end: datetime):
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Inputs must be datetime objects")
        if end < start:
            raise ValueError("End date must be after start date")
        self._start = start
        self._end = end

    @staticmethod
    def _is_birthday_passed(current: datetime, reference: datetime) -> bool:
        return (current.month, current.day) >= (reference.month, reference.day)

    def calculate(self) -> int:
        raw_diff = self._end.year - self._start.year
        if raw_diff == 0:
            return self._MIN_YEAR_DIFF
        if self._is_birthday_passed(self._end, self._start):
            return raw_diff
        return raw_diff - self._YEAR_CORRECTION

if __name__ == '__main__':
    start_dt = datetime(2010, 5, 20)
    end_dt = datetime(2023, 5, 19)
    calc = YearSpanCalculator(start_dt, end_dt)
    print(calc.calculate())