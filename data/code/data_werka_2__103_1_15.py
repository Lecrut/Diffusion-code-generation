import time

HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
MILLIS_IN_SECOND = 1000

MILLIS_PER_HOUR = HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * MILLIS_IN_SECOND
MILLIS_PER_HOUR_ACTUAL = MINUTES_IN_HOUR * SECONDS_IN_MINUTE * MILLIS_IN_SECOND
MILLIS_PER_MINUTE = SECONDS_IN_MINUTE * MILLIS_IN_SECOND

def get_milliseconds_elapsed_today() -> int:
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    millisecond = current_time.tm_msec
    
    if not (0 <= hour < 24):
        raise ValueError("Invalid hour")
    if not (0 <= minute < 60):
        raise ValueError("Invalid minute")
    if not (0 <= second < 60):
        raise ValueError("Invalid second")
        
    total_millis = (hour * MILLIS_PER_HOUR_ACTUAL) + \
                   (minute * MILLIS_PER_MINUTE) + \
                   (second * MILLIS_IN_SECOND) + \
                   millisecond
    return total_millis

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)