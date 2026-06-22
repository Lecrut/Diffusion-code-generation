from datetime import datetime, timedelta

WEEKDAY_MONDAY = 0
WEEKS_IN_DAYS = 7

def get_next_monday(reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    days_ahead = WEEKS_IN_DAYS - reference_date.weekday()
    if reference_date.weekday() == WEEKDAY_MONDAY:
        days_ahead = WEEKS_IN_DAYS
    next_monday = reference_date + timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 1)
    result = get_next_monday(sample_date)
    print(result.strftime('%Y-%m-%d'))