from datetime import datetime

class YearSpanCalculator:
    _MIN_YEAR_DIFF = 0

    def __init__(self, start: datetime, end: datetime):
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Inputs must be datetime objects")
        if end < start:
            raise ValueError("End date must be after start date")
        self.start = start
        self.end = end

    @staticmethod
    def _compare_month_day(date: datetime) -> tuple:
        return (date.month, date.day)

    def get_difference(self) -> int:
        raw_diff = self.end.year - self.start.year
        if raw_diff == 0:
            return self._MIN_YEAR_DIFF
        start_md = self._compare_month_day(self.start)
        end_md = self._compare_month_day(self.end)
        if end_md < start_md:
            return raw_diff - 1
        return raw_diff

if __name__ == '__main__':
    s = datetime(2010, 5, 10)
    e = datetime(2023, 5, 9)
    calc = YearSpanCalculator(s, e)
    print(calc.get_difference())