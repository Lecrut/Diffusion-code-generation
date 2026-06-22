from datetime import datetime, timedelta

def get_seconds_since_day_start(reference_date=None):
    if reference_date is None:
        reference_date = datetime(2024, 1, 15, 12, 30, 45)
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    start_of_day = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_date - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    sample_date = datetime(2024, 1, 15, 12, 30, 45)
    result = get_seconds_since_day_start(sample_date)
    print(result)