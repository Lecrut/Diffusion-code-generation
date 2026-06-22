import time
import calendar

def get_seconds_elapsed_since_midnight():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    seconds_since_midnight = (
        local_time.tm_hour * 3600 +
        local_time.tm_min * 60 +
        local_time.tm_sec
    )
    return seconds_since_midnight

if __name__ == '__main__':
    elapsed_seconds = get_seconds_elapsed_since_midnight()
    print(elapsed_seconds)