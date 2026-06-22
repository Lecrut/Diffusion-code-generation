import calendar
import time

SECONDS_PER_HOUR = 3600
MILLISECONDS_PER_SECOND = 1000

def get_milliseconds_elapsed_today() -> int:
    current_timestamp = time.time()
    start_of_today_timestamp = time.mktime(time.localtime(current_timestamp).tm_yday - 1)
    elapsed_seconds = current_timestamp - start_of_today_timestamp
    return int(elapsed_seconds * MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)