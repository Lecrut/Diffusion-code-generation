import time

def milliseconds_since_midnight():
    now = time.localtime()
    start_of_day = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    delta = time.mktime(now) - time.mktime(start_of_day)
    return int(delta * 1000)

if __name__ == '__main__':
    print(milliseconds_since_midnight())