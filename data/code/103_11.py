import time
import datetime
def calculate_elapsed_time_today():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_seconds = (now - start_of_day).total_seconds()
    return int(elapsed_seconds)
if __name__ == '__main__':
    print(calculate_elapsed_time_today())