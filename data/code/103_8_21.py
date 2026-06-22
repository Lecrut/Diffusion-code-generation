import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_elapsed_seconds_today() -> int:
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    total = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds
    return total

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)