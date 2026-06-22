from datetime import date
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class DateValidator:
    WEEK_START = Weekday.MONDAY
    WEEK_END = Weekday.FRIDAY

    @staticmethod
    def is_weekday(d: date) -> bool:
        if not isinstance(d, date):
            raise ValueError("Input must be a date instance")
        day_index = d.weekday()
        return DateValidator.WEEK_START <= day_index <= DateValidator.WEEK_END

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]
    for d in test_cases:
        print(DateValidator.is_weekday(d))