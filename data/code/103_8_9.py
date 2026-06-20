import time

def get_elapsed_seconds_today():
    current_time = time.localtime()
    start_of_day = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, 0, 0, 0))
    seconds_since_midnight = (time.mktime(current_time) - time.mktime(start_of_day)) // 1
    return int(seconds_since_midnight)

if __name__ == '__main__':
    elapsed_seconds = get_elapsed_seconds_today()
    print(f"Elapsed seconds since midnight: {elapsed_seconds}")