from datetime import datetime

def time_elapsed_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    if now < midnight:
        raise ValueError("Current time is before midnight")
    elapsed_seconds = (now - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    try:
        print(time_elapsed_since_midnight())
    except ValueError as e:
        print(e)