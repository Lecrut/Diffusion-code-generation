import time

def get_elapsed_seconds_today():
    now = time.localtime()
    start_of_day = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    elapsed_seconds = (time.mktime(now) - time.mktime(start_of_day)) // 1
    return int(elapsed_seconds)

if __name__ == '__main__':
    elapsed_seconds = get_elapsed_seconds_today()
    print(f"Elapsed seconds today: {elapsed_seconds}")