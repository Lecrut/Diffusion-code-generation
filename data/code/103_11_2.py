import time
import datetime
def calculate_elapsed_time_today():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = (now - start_of_day).total_seconds()
    return elapsed_time
if __name__ == '__main__':
    elapsed = calculate_elapsed_time_today()
    print(elapsed)