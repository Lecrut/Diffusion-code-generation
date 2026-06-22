import datetime
import time

def get_seconds_since_start_of_day():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    result = get_seconds_since_start_of_day()
    print(result)