from datetime import date, timedelta

WEEKEND_DAYS = {5, 6}

def _validate_date_input(d):
    if not isinstance(d, date):
        raise TypeError("Input must be a date object")
    if d < date.min or d > date.max:
        raise ValueError("Date out of valid range")
    return d

def find_next_weekend_date(start_date=None):
    if start_date is None:
        start_date = date.today()
    current = _validate_date_input(start_date)
    current = current.replace(day=1)
    next_day = current + timedelta(days=1)
    while next_day.weekday() not in WEEKEND_DAYS:
        next_day += timedelta(days=1)
    return next_day

if __name__ == '__main__':
    sample_date = date(2023, 10, 20)
    result = find_next_weekend_date(sample_date)
    print(result)