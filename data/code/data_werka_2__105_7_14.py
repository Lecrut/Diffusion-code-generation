from datetime import date, timedelta
from typing import Callable, TypeVar

DAY_INDEX_TUESDAY: int = 1
REFERENCE_DAY: int = 4
REFERENCE_MONTH: int = 7
REFERENCE_YEAR: int = 2023
DAYS_IN_WEEK: int = 7

TDate = TypeVar('TDate', bound=date)

def _get_upcoming_weekday(start_date: date, target_weekday: int) -> date:
    current_weekday: int = start_date.weekday()
    days_to_advance: int = (target_weekday - current_weekday) % DAYS_IN_WEEK
    if days_to_advance == 0:
        days_to_advance = DAYS_IN_WEEK
    return start_date + timedelta(days=days_to_advance)

def get_upcoming_tuesday_from_reference() -> date:
    reference_date: date = date(REFERENCE_YEAR, REFERENCE_MONTH, REFERENCE_DAY)
    return _get_upcoming_weekday(reference_date, DAY_INDEX_TUESDAY)

if __name__ == '__main__':
    upcoming_tuesday: date = get_upcoming_tuesday_from_reference()
    print(upcoming_tuesday)