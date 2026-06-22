import time

def get_elapsed_seconds_today() -> int:
    now = time.localtime()
    if now.tm_wday < 0 or now.tm_wday > 6:
        raise ValueError("Invalid weekday")
    if not (0 <= now.tm_hour <= 23):
        raise ValueError("Invalid hour")
    if not (0 <= now.tm_min <= 59):
        raise ValueError("Invalid minute")
    if not (0 <= now.tm_sec <= 59):
        raise ValueError("Invalid second")
    seconds_in_hour = 3600
    seconds_in_minute = 60
    elapsed = now.tm_hour * seconds_in_hour
    elapsed += now.tm_min * seconds_in_minute
    elapsed += now.tm_sec
    return elapsed

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)