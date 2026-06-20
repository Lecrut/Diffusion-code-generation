import time

def seconds_since_midnight():
    now = time.localtime()
    midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    return int(time.mktime(now) - time.mktime(midnight))

if __name__ == '__main__':
    print(seconds_since_midnight())