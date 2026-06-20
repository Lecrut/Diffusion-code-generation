import time

def get_elapsed_seconds_today():
    current_time = time.localtime()
    if not isinstance(current_time, time.struct_time):
        raise ValueError("Invalid time object")
    
    start_of_day = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    if not isinstance(start_of_day, time.struct_time):
        raise ValueError("Invalid start of day time object")
    
    time_difference = (current_time.tm_hour * 3600) + (current_time.tm_min * 60) + current_time.tm_sec
    return time_difference

if __name__ == '__main__':
    elapsed_seconds = get_elapsed_seconds_today()
    print(f"Elapsed seconds today: {elapsed_seconds}")