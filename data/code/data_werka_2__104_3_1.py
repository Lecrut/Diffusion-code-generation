from datetime import date
from typing import Tuple

def _sign(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def calculate_days_between(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    
    delta = d2 - d1
    return delta.days

def get_reference_dates() -> Tuple[date, date]:
    era_markers = {
        "start": date(2000, 1, 1),
        "end": date(2000, 1, 31)
    }
    return (era_markers["start"], era_markers["end"])

if __name__ == '__main__':
    ref_dates = get_reference_dates()
    start_date = ref_dates[0]
    end_date = ref_dates[1]
    
    computed_days = calculate_days_between(start_date, end_date)
    print(computed_days)