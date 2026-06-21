import time
import math

def get_elapsed_day_fraction():
    current = time.localtime()
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours_in_day = 24
    total_seconds_per_day = hours_in_day * minutes_in_hour * seconds_in_minute
    
    hours = current.tm_hour
    minutes = current.tm_min
    seconds = current.tm_sec
    
    if hours < 0 or hours >= hours_in_day:
        return 0.0
    if minutes < 0 or minutes >= minutes_in_hour:
        return 0.0
    if seconds < 0 or seconds >= seconds_in_minute:
        return 0.0
        
    elapsed_seconds = (hours * minutes_in_hour * seconds_in_minute) + (minutes * seconds_in_minute) + seconds
    return elapsed_seconds / total_seconds_per_day

if __name__ == '__main__':
    fraction = get_elapsed_day_fraction()
    print(fraction)