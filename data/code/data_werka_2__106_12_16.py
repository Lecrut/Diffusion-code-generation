from datetime import date
from typing import Tuple

YEARS_IN_A_DECADE = 10
DAYS_IN_YEAR_MIN = 365
DAYS_IN_YEAR_MAX = 366

def compute_exact_years_sep(d1: date, d2: date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    delta_days = (d2 - d1).days
    approx_years = delta_days // DAYS_IN_YEAR_MIN
    if approx_years < YEARS_IN_A_DECADE:
        return approx_years
    actual_years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        actual_years -= 1
    return actual_years

if __name__ == '__main__':
    start = date(1990, 2, 28)
    end = date(2024, 3, 1)
    val = compute_exact_years_sep(start, end)
    print(val)