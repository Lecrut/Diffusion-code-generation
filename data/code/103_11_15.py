import datetime
import time

def get_seconds_since_midnight() -> float:
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return (now - midnight).total_seconds()

if __name__ == '__main__':
    seconds = get_seconds_since_midnight()
    print(seconds)