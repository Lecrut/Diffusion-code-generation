from datetime import date
from typing import Tuple

class DateDuration:
    _YEAR_THRESHOLD = 365.2425

    @staticmethod
    def _normalize_years(start: date, end: date) -> Tuple[int, float]:
        days_diff = (end - start).days
        full_years = int(days_diff / DateDuration._YEAR_THRESHOLD)
        remainder_days = days_diff % DateDuration._YEAR_THRESHOLD
        fraction = remainder_days / DateDuration._YEAR_THRESHOLD
        return full_years, fraction

    @staticmethod
    def calculate_precise_years(start: date, end: date) -> float:
        if not isinstance(start, date) or not isinstance(end, date):
            raise ValueError("Inputs must be date objects")
        if start > end:
            raise ValueError("start must be before end")
        
        full_years, fraction = DateDuration._normalize_years(start, end)
        adjusted_years = full_years + fraction
        
        if start.month == end.month and start.day == end.day:
            adjusted_years = float(end.year - start.year)
            
        return adjusted_years

if __name__ == '__main__':
    start_date = date(2000, 1, 1)
    end_date = date(2023, 12, 31)
    result = DateDuration.calculate_precise_years(start_date, end_date)
    print(result)