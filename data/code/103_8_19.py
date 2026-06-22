import time

def get_elapsed_seconds_today() -> int:
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min
    second = now.tm_sec
    if hour < 0 or hour > 23:
        raise ValueError("Invalid hour")
    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute")
    if second < 0 or second > 59:
        raise ValueError("Invalid second")
    return hour * 3600 + minute * 60 + second

if __name__ == '__main__':
    elapsed = get_elapsed_seconds_today()
    print(elapsed)