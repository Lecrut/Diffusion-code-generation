import time

def get_milliseconds_elapsed_today() -> int:
    current = time.localtime()
    if not (0 <= current.tm_hour <= 23):
        raise ValueError("Invalid hour")
    if not (0 <= current.tm_min <= 59):
        raise ValueError("Invalid minute")
    if not (0 <= current.tm_sec <= 59):
        raise ValueError("Invalid second")
    hours = current.tm_hour
    minutes = current.tm_min
    seconds = current.tm_sec
    millis = current.tm_msec
    total = (hours * 3600000) + (minutes * 60000) + (seconds * 1000) + millis
    return total

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)