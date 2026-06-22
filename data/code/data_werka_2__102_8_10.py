from datetime import datetime
from typing import ClassVar

class DateValidator:
    WEEKDAY_LIMIT: ClassVar[int] = 5

    @staticmethod
    def parse_date(date_string: str) -> datetime:
        return datetime.fromisoformat(date_string)

    @staticmethod
    def is_weekday(date_string: str) -> bool:
        parsed_date = DateValidator.parse_date(date_string)
        return parsed_date.weekday() < DateValidator.WEEKDAY_LIMIT

if __name__ == '__main__':
    sample_dates = ["2023-10-06", "2023-10-07", "2023-10-08"]
    for date_str in sample_dates:
        result = DateValidator.is_weekday(date_str)
        print(result)