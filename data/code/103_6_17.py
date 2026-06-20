import time

def seconds_elapsed_today():
    now = time.time()
    midnight = int(time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst)))
    return int(now - midnight)

if __name__ == '__main__':
    print(seconds_elapsed_today())