import datetime
import decimal

SECONDS_PER_HOUR = 3600
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def compute_fractional_day_seconds(target_datetime=None):
    if target_datetime is None:
        target_datetime = datetime.datetime.now()
    
    if not isinstance(target_datetime, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    
    start_of_day = target_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    
    delta = target_datetime - start_of_day
    
    seconds = delta.seconds
    microseconds = delta.microseconds
    
    high_precision_seconds = decimal.Decimal(seconds) + (decimal.Decimal(microseconds) / decimal.Decimal(1000000))
    
    return float(high_precision_seconds)

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 12, 30, 45, 123456)
    result = compute_fractional_day_seconds(sample_dt)
    print(result)