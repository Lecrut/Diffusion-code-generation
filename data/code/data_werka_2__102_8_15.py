from datetime import datetime
from typing import Final

WEEKDAY_END: Final[int] = 5

class DateValidator:
    @staticmethod
    def is_weekday(date_string: str) -> bool:
        parsed_date = datetime.fromisoformat(date_string)
        return parsed_date.weekday() < WEEKDAY_END

if __name__ == '__main__':
    test_dates = [
        "2023-10-06",
        "2023-10-07",
        "2023-10-08",
        "2023-10-09",
        "2023-10-10",
        "2023-10-11",
        "2023-10-12"
    ]
    validator = DateValidator()
    for date_str in test_dates:
        result = validator.is_weekday(date_str)
        print(result)