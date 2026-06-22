from datetime import datetime

YEAR_OFFSETS = {
    "start": 0,
    "end": 0
}

def compute_year_span(reference_date: datetime, target_date: datetime) -> int:
    base_years = target_date.year - reference_date.year
    month_day_comparison = (target_date.month, target_date.day)
    reference_month_day = (reference_date.month, reference_date.day)
    if month_day_comparison < reference_month_day:
        base_years -= 1
    return base_years

if __name__ == '__main__':
    ref = datetime(1995, 6, 15)
    tgt = datetime(2024, 6, 14)
    span = compute_year_span(ref, tgt)
    print(span)