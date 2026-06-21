from datetime import datetime
from enum import IntEnum

class WeekdayStatus(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class DateValidator:
    WEEKDAY_LIMIT = 5

    @staticmethod
    def is_weekday(date_string: str) -> bool:
        parsed_date = datetime.fromisoformat(date_string)
        return parsed_date.weekday() < DateValidator.WEEKDAY_LIMIT

if __name__ == '__main__':
    test_dates = ["2023-10-06", "2023-10-07", "2023-10-08", "2023-10-09", "2023-10-10"]
    for date_str in test_dates:
        print(DateValidator.is_weekday(date_str))