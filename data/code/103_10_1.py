import datetime
import time
if __name__ == '__main__':
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_elapsed = now - midnight
    print(time_elapsed)