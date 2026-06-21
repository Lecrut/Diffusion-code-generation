import time
import calendar

def get_seconds_since_midnight():
    now = time.time()
    local_time = time.localtime(now)
    if local_time.tm_isdst is None or not local_time.tm_isdst:
        tz_offset = calendar.timegm(local_time) - now
    else:
        tz_offset = calendar.timegm(local_time) - now
    midnight_timestamp = now - tz_offset
    return now - midnight_timestamp

if __name__ == '__main__':
    result = get_seconds_since_midnight()
    print(result)