import time

def elapsed_time_from_midnight():
    now = time.localtime()
    midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    return (time.mktime(now) - time.mktime(midnight))

if __name__ == '__main__':
    print(elapsed_time_from_midnight())