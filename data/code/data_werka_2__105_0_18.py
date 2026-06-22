from datetime import datetime, timedelta

DAY_MONDAY = 0

def get_next_monday(reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    current_weekday = reference_date.weekday()
    days_ahead = (DAY_MONDAY - current_weekday) % 7
    if days_ahead == 0:
        days_ahead = 7
    return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    result = get_next_monday(sample_date)
    print(result.strftime('%Y-%m-%d'))