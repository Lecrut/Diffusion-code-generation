from datetime import datetime

class YearSpanCalculator:
    _MIN_YEAR_DIFF = 0
    _ADJUSTMENT_THRESHOLD = 1

    def __init__(self, start: datetime, end: datetime):
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Inputs must be datetime objects")
        if end < start:
            raise ValueError("End date must be after start date")
        self.start = start
        self.end = end

    @staticmethod
    def _is_birthday_passed(current: datetime, birth: datetime) -> bool:
        return (current.month, current.day) >= (birth.month, birth.day)

    def calculate(self) -> int:
        raw_diff = self.end.year - self.start.year
        if raw_diff == 0:
            return self._MIN_YEAR_DIFF
        if not self._is_birthday_passed(self.end, self.start):
            return raw_diff - self._ADJUSTMENT_THRESHOLD
        return raw_diff

if __name__ == '__main__':
    start_dt = datetime(2010, 5, 20)
    end_dt = datetime(2023, 5, 19)
    calc = YearSpanCalculator(start_dt, end_dt)
    print(calc.calculate())