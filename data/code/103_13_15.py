import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

def validate_time_components(hour, minute, second):
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23")
    if not (0 <= minute <= 59):
        raise ValueError("Minute must be between 0 and 59")
    if not (0 <= second <= 59):
        raise ValueError("Second must be between 0 and 59")

def compute_day_fraction():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    validate_time_components(hour, minute, second)
    elapsed_seconds = (hour * SECONDS_IN_HOUR) + (minute * 60) + second
    fraction = elapsed_seconds / SECONDS_IN_DAY
    return fraction

if __name__ == '__main__':
    result = compute_day_fraction()
    print(result)