from datetime import date, timedelta
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

DAYS_IN_WEEK = 7

def find_next_weekday(target_day: Weekday, current_date: date) -> date:
    current_weekday = current_date.weekday()
    days_to_add = (target_day - current_weekday + DAYS_IN_WEEK) % DAYS_IN_WEEK
    if days_to_add == 0:
        days_to_add = DAYS_IN_WEEK
    return current_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target = Weekday.THURSDAY
    result_date = find_next_weekday(target, start_date)
    print(result_date)