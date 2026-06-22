import time

def get_seconds_since_day_start() -> float:
    now = time.time()
    seconds_in_day = 86400
    seconds_since_start = now % seconds_in_day
    return seconds_since_start

if __name__ == '__main__':
    result = get_seconds_since_day_start()
    print(result)