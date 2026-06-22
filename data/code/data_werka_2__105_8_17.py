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

def validate_weekday(day: int) -> int:
    if not isinstance(day, int) or day < 0 or day > 6:
        raise ValueError("Day of week must be an integer between 0 and 6")
    return day

def find_next_weekday(start_date: date, target_day: int) -> date:
    valid_target = validate_weekday(target_day)
    current_weekday = start_date.weekday()
    days_to_add = (valid_target - current_weekday) % 7
    if days_to_add == 0:
        return start_date
    return start_date.replace() + timedelta(days=days_to_add)

from datetime import timedelta

def find_next_occurrence(target_day: int, start_date: date) -> date:
    return find_next_weekday(start_date, target_day)

if __name__ == '__main__':
    start = date(2023, 9, 15)
    result = find_next_occurrence(Weekday.THURSDAY, start)
    print(result)