import time

def milliseconds_since_midnight():
    current_time = time.localtime()
    start_of_day = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    milliseconds_passed = (time.mktime(current_time) - time.mktime(start_of_day)) * 1000
    return int(milliseconds_passed)

if __name__ == '__main__':
    milliseconds = milliseconds_since_midnight()
    print(milliseconds)