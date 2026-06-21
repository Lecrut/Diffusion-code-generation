from datetime import datetime

def compute_year_diff(reference: datetime, target: datetime) -> int:
    if not isinstance(reference, datetime):
        raise ValueError("reference must be a datetime instance")
    if not isinstance(target, datetime):
        raise ValueError("target must be a datetime instance")
    year_span = target.year - reference.year
    if target.month < reference.month:
        year_span -= 1
    elif target.month == reference.month and target.day < reference.day:
        year_span -= 1
    return year_span

if __name__ == '__main__':
    base = datetime(1990, 6, 15)
    current = datetime(2023, 5, 28)
    diff = compute_year_diff(base, current)
    print(diff)