from datetime import date
from typing import Tuple

class DateCalculator:
    _MIN_YEAR = 1
    _MAX_YEAR = 9999

    @staticmethod
    def _validate_date(d: date) -> None:
        if not isinstance(d, date):
            raise TypeError("Input must be a datetime.date object")
        if d.year < DateCalculator._MIN_YEAR or d.year > DateCalculator._MAX_YEAR:
            raise ValueError("Date out of range")

    @classmethod
    def compute_years_difference(cls, start: date, end: date) -> int:
        cls._validate_date(start)
        cls._validate_date(end)

        if start > end:
            start, end = end, start

        year_diff = end.year - start.year
        start_anniversary = date(end.year, start.month, start.day)

        if end < start_anniversary:
            year_diff -= 1

        return year_diff

if __name__ == '__main__':
    start_date = date(1990, 2, 28)
    end_date = date(2024, 2, 27)
    calculator = DateCalculator()
    diff = calculator.compute_years_difference(start_date, end_date)
    print(diff)