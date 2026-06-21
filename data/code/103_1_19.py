import time

def get_milliseconds_elapsed_today() -> int:
    seconds_per_minute = 60
    milliseconds_per_second = 1000
    
    current = time.localtime()
    
    hours = current.tm_hour
    minutes = current.tm_min
    seconds = current.tm_sec
    milliseconds = current.tm_msec
    
    if not (0 <= hours <= 23):
        raise ValueError("Hour out of range")
    if not (0 <= minutes <= 59):
        raise ValueError("Minute out of range")
    if not (0 <= seconds <= 59):
        raise ValueError("Second out of range")
    if not (0 <= milliseconds <= 999):
        raise ValueError("Millisecond out of range")
        
    total_seconds_from_midnight = (hours * seconds_per_minute + minutes) * seconds_per_minute + seconds
    total_milliseconds = total_seconds_from_midnight * milliseconds_per_second + milliseconds
    
    return total_milliseconds

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)