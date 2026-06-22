import datetime
import calendar

UNIT_MAP = {
    'fraction': 1.0,
    'seconds': 86400,
    'minutes': 1440,
    'hours': 24,
    'days': 1
}

def compute_time_metrics(reference_dt=None):
    if reference_dt is None:
        reference_dt = datetime.datetime.now()
    if not isinstance(reference_dt, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    start_of_day = reference_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_dt - start_of_day
    total_seconds = delta.total_seconds()
    days_in_month = calendar.monthrange(reference_dt.year, reference_dt.month)[1]
    day_of_month = reference_dt.day
    fractional_day = total_seconds / 86400
    metrics = {
        'fractional_day_passed': fractional_day,
        'seconds_passed': total_seconds,
        'current_day_of_month': day_of_month,
        'total_days_in_month': days_in_month
    }
    return metrics

if __name__ == '__main__':
    sample_time = datetime.datetime(2024, 11, 15, 14, 30, 45, 500000)
    output = compute_time_metrics(sample_time)
    print(output['fractional_day_passed'])
    print(output['seconds_passed'])
    print(output['current_day_of_month'])
    print(output['total_days_in_month'])