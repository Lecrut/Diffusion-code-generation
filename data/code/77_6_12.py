from datetime import datetime

MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def elapsed_minutes_since_midnight(dt):
    midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return (dt - midnight).seconds // SECONDS_PER_MINUTE + (dt - midnight).days * MINUTES_PER_HOUR

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    print(elapsed_minutes_since_midnight(sample_dt))