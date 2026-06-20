import time

def elapsed_seconds_today():
    now = time.localtime()
    start_of_day = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    return int(time.mktime(now) - time.mktime(start_of_day))

if __name__ == '__main__':
    print(elapsed_seconds_today())