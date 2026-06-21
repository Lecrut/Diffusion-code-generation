import datetime
import time

UNIT_MAP = {
    'fractional_day': 1.0,
    'seconds': 86400.0,
    'milliseconds': 86400000.0,
    'microseconds': 86400000000.0
}

def compute_time_metrics(reference_time=None):
    if reference_time is None:
        reference_time = datetime.datetime.now()
    
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    total_seconds = delta.total_seconds()
    
    fractional_day = total_seconds / UNIT_MAP['seconds']
    
    metrics = {}
    for unit_name, divisor in UNIT_MAP.items():
        if unit_name == 'fractional_day':
            metrics[unit_name] = fractional_day
        else:
            metrics[unit_name] = total_seconds * (UNIT_MAP[unit_name] / UNIT_MAP['seconds'])
            
    return metrics

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 11, 15, 14, 30, 15, 500000)
    results = compute_time_metrics(sample_dt)
    print(results)