from datetime import datetime, time

def compute_elapsed_seconds_since_midnight(reference_datetime: datetime) -> int:
    if not isinstance(reference_datetime, datetime):
        raise ValueError("reference_datetime must be a datetime instance")
    
    start_of_day = datetime.combine(reference_datetime.date(), time.min)
    
    if reference_datetime < start_of_day:
        raise ValueError("reference_datetime cannot be before start of day")
        
    delta = reference_datetime - start_of_day
    return int(delta.total_seconds())

if __name__ == '__main__':
    sample_dt = datetime(2024, 11, 15, 13, 45, 30)
    elapsed = compute_elapsed_seconds_since_midnight(sample_dt)
    print(elapsed)