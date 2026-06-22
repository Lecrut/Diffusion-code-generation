import time

def get_elapsed_seconds_today() -> int:
    local_time = time.localtime()
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    total = (hour * 60 + minute) * 60 + second
    return total

if __name__ == '__main__':
    print(get_elapsed_seconds_today())