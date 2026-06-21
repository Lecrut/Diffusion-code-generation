from datetime import date
from enum import IntEnum

class DayIndex(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class DateValidator:
    WEEK_START = DayIndex.MONDAY
    WEEK_END = DayIndex.FRIDAY

    @staticmethod
    def is_business_day(d: date) -> bool:
        if not isinstance(d, date):
            raise ValueError("Input must be a date object")
        day_num = d.weekday()
        return DateValidator.WEEK_START <= day_num <= DateValidator.WEEK_END

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 24),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]
    for d in test_cases:
        print(DateValidator.is_business_day(d))