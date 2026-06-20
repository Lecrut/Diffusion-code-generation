import time

def elapsed_seconds_today():
    current_time = time.localtime()
    start_of_day = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, 0, 0, 0))
    seconds_since_midnight = int(time.mktime(current_time) - time.mktime(start_of_day))
    return seconds_since_midnight

if __name__ == '__main__':
    print(f"Elapsed seconds today: {elapsed_seconds_today()}")