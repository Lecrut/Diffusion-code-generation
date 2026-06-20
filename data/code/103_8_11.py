import time

def validate_input(value):
    if not isinstance(value, time.struct_time):
        raise ValueError("Input must be of type time.struct_time")

def get_elapsed_seconds_today(localtime=None):
    validate_input(time.localtime() if localtime is None else localtime)
    start_of_day = time.struct_time((localtime.tm_year, localtime.tm_mon, localtime.tm_mday, 0, 0, 0, localtime.tm_wday, localtime.tm_yday, localtime.tm_isdst))
    elapsed_seconds = (localtime.tm_hour * 3600) + (localtime.tm_min * 60) + localtime.tm_sec
    return elapsed_seconds

if __name__ == '__main__':
    sample_localtime = time.localtime(1698492510)
    print(f"Elapsed seconds today: {get_elapsed_seconds_today(sample_localtime)}")