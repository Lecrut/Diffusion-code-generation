import time

def seconds_since_midnight():
    current_time = time.localtime()
    midnight_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    return int(time.mktime(current_time) - time.mktime(midnight_time))

if __name__ == '__main__':
    print(seconds_since_midnight())