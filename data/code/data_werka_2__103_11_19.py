import time
import datetime

def get_seconds_since_midnight():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - start_of_day
    return elapsed.total_seconds()

if __name__ == '__main__':
    elapsed_seconds = get_seconds_since_midnight()
    print(elapsed_seconds)