import datetime

def compute_seconds_since_midnight() -> float:
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - midnight
    return elapsed.total_seconds()

if __name__ == '__main__':
    result = compute_seconds_since_midnight()
    print(result)