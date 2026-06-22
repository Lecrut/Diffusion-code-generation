from datetime import date
from typing import Tuple

YEAR_MAPPING = {
    "start": date(1, 1, 1),
    "end": date(9999, 12, 31),
    "reference": date(2021, 6, 15),
    "target": date(2025, 12, 25)
}

def compute_year_span(reference_date: date, target_date: date) -> int:
    delta_days = (target_date - reference_date).days
    years_approx = delta_days // 365
    return abs(years_approx)

if __name__ == '__main__':
    ref = YEAR_MAPPING["reference"]
    tgt = YEAR_MAPPING["target"]
    span = compute_year_span(ref, tgt)
    print(span)