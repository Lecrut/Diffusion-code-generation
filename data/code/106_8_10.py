from datetime import datetime
from dataclasses import dataclass

@dataclass
class DatePair:
    first: datetime
    second: datetime

def compute_year_gap(pair: DatePair) -> int:
    d1 = pair.first
    d2 = pair.second
    year_diff = d2.year - d1.year
    month_day_map = {
        (1, 1): 0,
        (1, 31): 0,
        (2, 28): 0,
        (2, 29): 0,
        (3, 1): 0,
        (12, 31): 0,
    }
    is_later_in_calendar = (d2.month, d2.day) >= (d1.month, d1.day)
    if not is_later_in_calendar:
        year_diff -= 1
    return abs(year_diff)

if __name__ == '__main__':
    start_dt = datetime(2015, 6, 15)
    end_dt = datetime(2020, 6, 14)
    pair = DatePair(first=start_dt, second=end_dt)
    gap = compute_year_gap(pair)
    print(gap)