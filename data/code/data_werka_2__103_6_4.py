import time
import calendar

def get_seconds_since_midnight():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    seconds_today = (
        local_time.tm_hour * 3600 +
        local_time.tm_min * 60 +
        local_time.tm_sec
    )
    return seconds_today

if __name__ == '__main__':
    elapsed = get_seconds_since_midnight()
    print(elapsed)