from datetime import date
from typing import NamedTuple

class DateInterval(NamedTuple):
    start: date
    end: date

def get_days_delta(interval: DateInterval) -> int:
    if not isinstance(interval.start, date) or not isinstance(interval.end, date):
        raise ValueError("Dates must be datetime.date instances")
    return (interval.end - interval.start).days

if __name__ == '__main__':
    era_names = {
        "q1_2023": DateInterval(date(2023, 1, 1), date(2023, 3, 31)),
        "q2_2023": DateInterval(date(2023, 4, 1), date(2023, 6, 30)),
    }
    for name, interval in era_names.items():
        print(f"{name}: {get_days_delta(interval)}")