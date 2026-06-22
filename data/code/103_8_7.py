import time

def get_elapsed_seconds_today() -> int:
    now = time.localtime()
    seconds_in_day = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
    return seconds_in_day

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)