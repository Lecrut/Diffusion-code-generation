import time

def get_elapsed_seconds_today() -> int:
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)