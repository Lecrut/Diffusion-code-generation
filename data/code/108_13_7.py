from datetime import date
from typing import NamedTuple

_MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

class DateRecord(NamedTuple):
    year: int
    month: int
    day: int

def get_day_numeric(record: DateRecord) -> int:
    return record.day

if __name__ == '__main__':
    target = DateRecord(year=2024, month=10, day=10)
    day_value = get_day_numeric(target)
    print(day_value)