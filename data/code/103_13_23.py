import time

def get_day_fraction():
    current = time.localtime()
    seconds_in_hour = 3600
    minutes_in_hour = 60
    total_seconds_in_day = 86400
    elapsed = (current.tm_hour * seconds_in_hour) + (current.tm_min * minutes_in_hour) + current.tm_sec
    return elapsed / total_seconds_in_day

if __name__ == '__main__':
    print(get_day_fraction())