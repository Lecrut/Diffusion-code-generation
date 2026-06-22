from time import time
from datetime import datetime, timedelta

def get_time_elapsed_since_midnight():
    now = time()
    midnight = datetime.fromtimestamp(now - (now % 86400))
    current_dt = datetime.fromtimestamp(now)
    delta = current_dt - midnight
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    elapsed = get_time_elapsed_since_midnight()
    print(elapsed)