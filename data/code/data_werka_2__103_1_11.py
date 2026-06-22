import time
def get_milliseconds_elapsed_today() -> int:
    units = {
        "hour": 3600000,
        "minute": 60000,
        "second": 1000
    }
    now = time.localtime()
    total = 0
    total += now.tm_hour * units["hour"]
    total += now.tm_min * units["minute"]
    total += now.tm_sec * units["second"]
    total += now.tm_msec
    return total
if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)