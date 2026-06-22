import time

UNIT_SECONDS = 1
UNIT_MINUTES = 60
UNIT_HOURS = 3600

TIME_UNITS = {
    "hour": UNIT_HOURS,
    "minute": UNIT_MINUTES,
    "second": UNIT_SECONDS
}

def calculate_seconds_from_midnight():
    current_time_tuple = time.localtime()
    seconds_elapsed = (
        current_time_tuple.tm_hour * TIME_UNITS["hour"] +
        current_time_tuple.tm_min * TIME_UNITS["minute"] +
        current_time_tuple.tm_sec
    )
    return seconds_elapsed

if __name__ == '__main__':
    result = calculate_seconds_from_midnight()
    print(result)