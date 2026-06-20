import time

def get_localtime():
    return time.localtime()

def is_valid_time_struct(tm):
    return all(isinstance(i, int) for i in tm[:6])

def calculate_elapsed_seconds_today(tm):
    if not is_valid_time_struct(tm):
        raise ValueError("Invalid time struct")
    start_of_day = (tm.tm_year, tm.tm_mon, tm.tm_mday, 0, 0, 0, tm.tm_wday, tm.tm_yday, tm.tm_isdst)
    elapsed_seconds = sum((start_of_day[i] - tm[i]) * multiplier for i, multiplier in enumerate([31536000, 2628000, 86400, 3600, 60, 1]))
    return int(elapsed_seconds)

if __name__ == '__main__':
    current_time = get_localtime()
    elapsed_seconds = calculate_elapsed_seconds_today(current_time)
    print(f"Elapsed seconds today: {elapsed_seconds}")