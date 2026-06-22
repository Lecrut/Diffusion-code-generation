import time

def calculate_day_fraction():
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    milliseconds = now.tm_sec % 1
    total_seconds_in_day = 86400
    current_seconds = (hours * 3600) + (minutes * 60) + seconds
    return current_seconds / total_seconds_in_day

if __name__ == '__main__':
    fraction = calculate_day_fraction()
    print(fraction)