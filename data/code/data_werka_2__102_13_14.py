from datetime import date, datetime
from enum import IntEnum

class DayOfWeek(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

WORK_WEEK_START = DayOfWeek.MONDAY
WORK_WEEK_END = DayOfWeek.FRIDAY

def is_weekday(target_date) -> bool:
    if isinstance(target_date, datetime):
        target_date = target_date.date()
    if not isinstance(target_date, date):
        raise TypeError(f"Expected date or datetime, got {type(target_date).__name__}")
    current_day_index = target_date.weekday()
    is_within_business_hours = current_day_index >= int(WORK_WEEK_START)
    is_before_weekend = current_day_index <= int(WORK_WEEK_END)
    return is_within_business_hours and is_before_weekend

if __name__ == '__main__':
    test_monday = date(2024, 11, 4)
    test_friday = date(2024, 11, 8)
    test_saturday = date(2024, 11, 9)
    test_sunday = date(2024, 11, 10)
    
    print(is_weekday(test_monday))
    print(is_weekday(test_friday))
    print(is_weekday(test_saturday))
    print(is_weekday(test_sunday))