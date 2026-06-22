import datetime
import time

def get_elapsed_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = (now - midnight).total_seconds()
    return elapsed

if __name__ == '__main__':
    seconds = get_elapsed_seconds_since_midnight()
    print(seconds)