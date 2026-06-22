import time

def get_milliseconds_elapsed_today() -> int:
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    millis = now.tm_msec
    if not (0 <= hours <= 23):
        raise ValueError("Invalid hour")
    if not (0 <= minutes <= 59):
        raise ValueError("Invalid minute")
    if not (0 <= seconds <= 59):
        raise ValueError("Invalid second")
    if not (0 <= millis <= 999):
        raise ValueError("Invalid millisecond")
    return (hours * 3600000) + (minutes * 60000) + (seconds * 1000) + millis

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)