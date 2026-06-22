import datetime
import time

def get_fractional_day_seconds():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    return total_seconds

if __name__ == '__main__':
    result = get_fractional_day_seconds()
    print(result)