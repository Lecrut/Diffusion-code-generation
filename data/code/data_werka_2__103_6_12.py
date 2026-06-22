import datetime
import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def calculate_seconds_since_midnight():
    current_time = time.localtime()
    seconds_elapsed = (
        current_time.tm_hour * SECONDS_IN_HOUR +
        current_time.tm_min * SECONDS_IN_MINUTE +
        current_time.tm_sec
    )
    return seconds_elapsed

if __name__ == '__main__':
    elapsed_seconds = calculate_seconds_since_midnight()
    print(elapsed_seconds)