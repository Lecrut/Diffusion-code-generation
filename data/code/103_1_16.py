import time

def get_milliseconds_elapsed_today() -> int:
    current = time.localtime()
    hours = current.tm_hour
    minutes = current.tm_min
    seconds = current.tm_sec
    millis = current.tm_msec
    seconds_elapsed = (hours * 3600) + (minutes * 60) + seconds
    total_milliseconds = (seconds_elapsed * 1000) + millis
    return total_milliseconds

if __name__ == '__main__':
    sample_value = get_milliseconds_elapsed_today()
    print(sample_value)