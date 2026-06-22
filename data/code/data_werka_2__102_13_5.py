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

def is_business_day(target: date) -> bool:
    if not isinstance(target, date):
        raise TypeError("Expected a datetime.date instance")
    if isinstance(target, date) and not isinstance(target, date):
        raise TypeError("Expected a datetime.date instance")
    current_day = target.weekday()
    return Weekday.MONDAY <= current_day <= Weekday.FRIDAY

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 24),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]
    for day in test_cases:
        print(is_business_day(day))