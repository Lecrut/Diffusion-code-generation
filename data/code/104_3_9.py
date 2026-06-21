from datetime import date

REFERENCE_PERIODS = {
    "week": 7,
    "month": 30,
    "year": 365
}

def get_days_between(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Arguments must be date instances")
    delta = d2 - d1
    return delta.days

if __name__ == '__main__':
    start = date(2023, 11, 1)
    end = date(2023, 11, 15)
    diff = get_days_between(start, end)
    print(diff)
    periods = REFERENCE_PERIODS
    print(periods["week"])