import time

SECONDS_PER_MINUTE = 60
MILLISECONDS_PER_SECOND = 1000
MILLISECONDS_PER_MINUTE = SECONDS_PER_MINUTE * MILLISECONDS_PER_SECOND

MILLIS_MAP = {
    "second": MILLISECONDS_PER_SECOND,
    "minute": MILLISECONDS_PER_MINUTE,
    "hour": MILLISECONDS_PER_MINUTE * 60,
}

def get_milliseconds_elapsed_today() -> int:
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    millis = current_time.tm_msec

    elapsed_seconds = (hours * MILLIS_MAP["hour"]) + (minutes * MILLIS_MAP["minute"]) + (seconds * MILLIS_MAP["second"])
    total_milliseconds = elapsed_seconds + millis
    return total_milliseconds

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)