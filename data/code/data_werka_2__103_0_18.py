import datetime

def compute_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        raise ValueError("Time cannot be negative")
    return total_seconds

if __name__ == '__main__':
    result = compute_seconds_since_midnight()
    print(result)