import time

def get_elapsed_seconds_today():
    now = time.localtime()
    start_of_day = (now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst)
    elapsed_seconds = int(time.mktime(now) - time.mktime(start_of_day))
    return elapsed_seconds

if __name__ == '__main__':
    print(f"Elapsed seconds today: {get_elapsed_seconds_today()}")