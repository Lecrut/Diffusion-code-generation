from datetime import date
from typing import Tuple

class DateSpanCalculator:
    _MIN_YEAR: int = 1
    _MAX_YEAR: int = 9999

    @staticmethod
    def _validate_dates(start: date, end: date) -> None:
        if start.year < DateSpanCalculator._MIN_YEAR or start.year > DateSpanCalculator._MAX_YEAR:
            raise ValueError("Start year out of range")
        if end.year < DateSpanCalculator._MIN_YEAR or end.year > DateSpanCalculator._MAX_YEAR:
            raise ValueError("End year out of range")

    @staticmethod
    def _compute_difference(start: date, end: date) -> int:
        year_diff: int = end.year - start.year
        month_day_start: Tuple[int, int] = (start.month, start.day)
        month_day_end: Tuple[int, int] = (end.month, end.day)
        
        if month_day_end < month_day_start:
            year_diff -= 1
        
        return year_diff

    @classmethod
    def get_precise_years(cls, start_date: date, end_date: date) -> int:
        cls._validate_dates(start_date, end_date)
        if start_date > end_date:
            return -cls._compute_difference(end_date, start_date)
        return cls._compute_difference(start_date, end_date)

if __name__ == '__main__':
    start_dt: date = date(1990, 2, 28)
    end_dt: date = date(2024, 3, 1)
    years: int = DateSpanCalculator.get_precise_years(start_dt, end_dt)
    print(years)