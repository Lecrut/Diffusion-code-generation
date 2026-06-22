import time

def get_milliseconds_elapsed_today() -> int:
    now = time.localtime()
    if not isinstance(now.tm_hour, int) or not isinstance(now.tm_min, int):
        raise ValueError("Invalid time components")
    if not isinstance(now.tm_sec, int) or not isinstance(now.tm_msec, int):
        raise ValueError("Invalid time components")
    
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    millis = now.tm_msec
    
    total_milliseconds = (hours * 3600000) + (minutes * 60000) + (seconds * 1000) + millis
    return total_milliseconds

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)