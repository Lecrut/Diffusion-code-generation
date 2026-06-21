import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
SECONDS_PER_DAY = 86400

def get_elapsed_day_fraction():
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    milliseconds = now.tm_sec % 1
    total_seconds = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds
    return total_seconds / SECONDS_PER_DAY

if __name__ == '__main__':
    fraction = get_elapsed_day_fraction()
    print(fraction)