from datetime import datetime
from typing import Union

class DateExtractor:
    DAYS_IN_MONTHS: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_day_of_month(dt: datetime) -> int:
        if not isinstance(dt, datetime):
            raise ValueError("Input must be a datetime object")
        return dt.day

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29)
    extractor = DateExtractor()
    day_value = extractor.get_day_of_month(sample_dt)
    print(day_value)