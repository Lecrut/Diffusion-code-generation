from datetime import datetime

def elapsed_minutes_since_midnight(dt):
    if not isinstance(dt, datetime):
        raise TypeError("Input must be a datetime object.")
    midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return int((dt - midnight).total_seconds() / 60)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(elapsed_minutes_since_midnight(sample_dt))