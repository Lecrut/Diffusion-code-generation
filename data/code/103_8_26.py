import time

def get_elapsed_seconds_today():
    now = time.localtime()
    start_of_day = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, 0, 0, now.tm_isdst))
    current_time = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec, 0, 0, now.tm_isdst))
    elapsed = int(current_time - start_of_day)
    return elapsed

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)